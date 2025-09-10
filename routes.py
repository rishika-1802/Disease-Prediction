from flask import render_template, request, redirect, url_for, flash, session, make_response, jsonify
from app import app
from models import Prediction, ModelMetrics
from ml_model import predictor
from data_processor import data_processor
from utils.pdf_generator import generate_prediction_pdf
from utils.disease_info import get_disease_info
import json
import uuid
from datetime import datetime, timedelta
import logging
from app import db

# Initialize data when the module loads
data_processor.initialize_data()

@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Symptom input and prediction page"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name', '').strip()
            age = request.form.get('age')
            gender = request.form.get('gender')
            selected_symptoms = request.form.getlist('symptoms')
            
            # Validate required fields
            if not name:
                flash('Please enter your name.', 'error')
                return redirect(url_for('predict'))
            
            if not age or not age.isdigit() or int(age) < 1 or int(age) > 120:
                flash('Please enter a valid age (1-120).', 'error')
                return redirect(url_for('predict'))
                
            if not gender:
                flash('Please select your gender.', 'error')
                return redirect(url_for('predict'))
            
            if not selected_symptoms:
                flash('Please select at least one symptom.', 'error')
                return redirect(url_for('predict'))
                
            age = int(age)
            
            # Prepare symptoms dictionary
            symptoms_dict = {symptom: (1 if symptom in selected_symptoms else 0) for symptom in data_processor.get_symptoms_list()}
            
            # Make prediction
            result = predictor.predict(symptoms_dict)
            
            if result.get('success'):
                # Ensure session ID is present before storing
                if 'session_id' not in session:
                    session['session_id'] = str(uuid.uuid4())

                # Store prediction in database
                prediction = Prediction()
                prediction.name = name
                prediction.age = age
                prediction.gender = gender
                prediction.symptoms = json.dumps(selected_symptoms)
                prediction.predicted_disease = result['disease']
                prediction.confidence_score = result['confidence']
                prediction.session_id = session['session_id']
                
                db.session.add(prediction)
                db.session.commit()
                
                # Store result in session for result page
                session['last_prediction'] = {
                    'name': name,
                    'age': age,
                    'gender': gender,
                    'disease': result['disease'],
                    'confidence': result['confidence'],
                    'symptoms': selected_symptoms,
                    'prediction_id': prediction.id
                }
                
                return redirect(url_for('result'))
            else:
                flash(f'Prediction failed: {result.get("error", "Unknown error")}', 'error')
                
        except Exception as e:
            logging.error(f"Error in prediction: {str(e)}")
            flash('An error occurred during prediction. Please try again.', 'error')
    
    # GET request - show form
    symptoms_list = data_processor.get_symptoms_list()
    
    return render_template('predict.html', 
                            symptoms=symptoms_list)

@app.route('/result')
def result():
    """Display prediction result"""
    prediction_data = session.get('last_prediction')
    
    if not prediction_data:
        flash('No prediction data found. Please make a prediction first.', 'error')
        return redirect(url_for('predict'))
    
    # Get disease information
    disease_info = get_disease_info(prediction_data['disease'])
    
    return render_template('result.html', 
                            prediction=prediction_data,
                            disease_info=disease_info)

@app.route('/download_report')
def download_report():
    """Generate and download PDF report"""
    prediction_data = session.get('last_prediction')
    
    if not prediction_data:
        flash('No prediction data found. Please make a prediction first.', 'error')
        return redirect(url_for('predict'))
    
    try:
        # Generate PDF
        pdf_buffer = generate_prediction_pdf(prediction_data)
        
        # Create response
        response = make_response(pdf_buffer.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=disease_prediction_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        
        return response
        
    except Exception as e:
        logging.error(f"Error generating PDF: {str(e)}")
        flash('Error generating PDF report. Please try again.', 'error')
        return redirect(url_for('result'))

@app.route('/dashboard')
def dashboard():
    """Analytics dashboard"""
    try:
        # Get prediction statistics
        total_predictions = Prediction.query.count()
        
        # Recent predictions (last 30 days)
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        recent_predictions = Prediction.query.filter(
            Prediction.created_at >= thirty_days_ago
        ).count()
        
        # Disease distribution
        disease_counts = db.session.query(
            Prediction.predicted_disease,
            db.func.count(Prediction.id).label('count')
        ).group_by(Prediction.predicted_disease).order_by(db.desc('count')).all()
        
        disease_data = {
            'labels': [item[0] for item in disease_counts[:10]], 
            'data': [item[1] for item in disease_counts[:10]]
        }
        
        # Predictions over time (last 7 days)
        seven_days_ago = datetime.utcnow() - timedelta(days=7)
        daily_predictions = db.session.query(
            db.func.date(Prediction.created_at).label('date'),
            db.func.count(Prediction.id).label('count')
        ).filter(
            Prediction.created_at >= seven_days_ago
        ).group_by(db.func.date(Prediction.created_at)).order_by(db.asc('date')).all()

        # Fill in any missing dates with zero counts
        date_range = [datetime.utcnow().date() - timedelta(days=i) for i in range(6, -1, -1)]
        daily_counts_dict = {item[0]: item[1] for item in daily_predictions}
        
        time_data = {
            'labels': [date.strftime('%Y-%m-%d') for date in date_range],
            'data': [daily_counts_dict.get(date, 0) for date in date_range]
        }
        
        # Model metrics
        model_metrics = getattr(predictor, 'model_metrics', {
            'accuracy': 0.0,
            'precision': 0.0,
            'recall': 0.0,
            'f1_score': 0.0,
            'model_type': 'Random Forest'
        })

        return render_template('dashboard.html',
                               total_predictions=total_predictions,
                               recent_predictions=recent_predictions,
                               disease_data=disease_data,
                               time_data=time_data,
                               model_metrics=model_metrics)
                               
    except Exception as e:
        logging.error(f"Error loading dashboard: {str(e)}")
        flash('Error loading dashboard data.', 'error')
        # Pass empty dictionaries and zero values to the template
        return render_template('dashboard.html',
                               total_predictions=0,
                               recent_predictions=0,
                               disease_data={'labels': [], 'data': []},
                               time_data={'labels': [], 'data': []},
                               model_metrics={'accuracy': 0, 'precision': 0, 'recall': 0, 'f1_score': 0})

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        # In a real application, you would process the contact form
        # For now, just show a success message
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            flash('Thank you for your message. We will get back to you soon!', 'success')
        else:
            flash('Please fill in all fields.', 'error')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/api/retrain_model', methods=['POST'])
def retrain_model():
    """API endpoint to retrain the model"""
    try:
        df, success = predictor.load_and_preprocess_data()
        if success:
            metrics = predictor.train_model(df)
            if 'error' not in metrics:
                return jsonify({'success': True, 'metrics': metrics})
            else:
                return jsonify({'success': False, 'error': metrics['error']})
        else:
            return jsonify({'success': False, 'error': 'Failed to load data'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500