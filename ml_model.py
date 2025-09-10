import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os
import logging
from typing import Tuple, Dict, Any

class DiseasePredictor:
    def __init__(self):
        self.model = None
        self.feature_columns = []
        self.label_encoder = LabelEncoder()
        self.scaler = StandardScaler()
        self.is_trained = False
        self.model_metrics = {}

    def load_and_preprocess_data(self, file_path: str = 'synthetic_symptoms_dataset_realistic_100_diseases (3).xlsx') -> Tuple[pd.DataFrame, bool]:
        """Load and preprocess the dataset"""
        try:
            # Load Excel or fallback to sample
            if os.path.exists(file_path):
                df = pd.read_excel(file_path)
                logging.info(f"Loaded dataset with {len(df)} rows and {len(df.columns)} columns")
            else:
                logging.warning(f"Dataset file {file_path} not found. Using sample data.")
                df = self._create_sample_data()

            # Clean
            df = df.dropna()

            # ✅ Convert yes/no-like values to numeric (no FutureWarning)
            df = df.replace(
                {
                    'yes': 1, 'no': 0,
                    'Yes': 1, 'No': 0,
                    'Y': 1, 'N': 0,
                    'True': 1, 'False': 0
                }
            ).infer_objects(copy=False)

            # Identify target column
            target_col = 'Disease' if 'Disease' in df.columns else ('disease' if 'disease' in df.columns else df.columns[-1])
            self.feature_columns = [col for col in df.columns if col != target_col]

            logging.info(f"Target column: {target_col}")
            logging.info(f"Feature columns: {len(self.feature_columns)}")

            return df, True

        except Exception as e:
            logging.error(f"Error loading dataset: {str(e)}")
            df = self._create_sample_data()
            return df, False

    def _create_sample_data(self) -> pd.DataFrame:
        """Create sample data for fallback"""
        np.random.seed(42)
        symptoms = [
            'fever', 'cough', 'headache', 'fatigue', 'nausea', 'vomiting',
            'diarrhea', 'abdominal_pain', 'chest_pain', 'shortness_of_breath',
            'dizziness', 'muscle_aches', 'joint_pain', 'rash', 'sore_throat',
            'runny_nose', 'loss_of_appetite', 'weight_loss', 'night_sweats',
            'back_pain', 'constipation', 'blurred_vision', 'difficulty_swallowing',
            'excessive_thirst', 'frequent_urination'
        ]
        diseases = [
            'Common Cold', 'Influenza', 'COVID-19', 'Pneumonia', 'Bronchitis',
            'Gastroenteritis', 'Migraine', 'Hypertension', 'Diabetes',
            'Arthritis', 'Asthma', 'Allergic Rhinitis', 'Sinusitis',
            'UTI', 'Food Poisoning', 'Anxiety', 'Depression', 'Insomnia',
            'Acid Reflux', 'IBS'
        ]
        data = []
        for _ in range(1000):
            row = {symptom: np.random.choice([0, 1], p=[0.7, 0.3]) for symptom in symptoms}
            row['Disease'] = np.random.choice(diseases)
            data.append(row)

        df = pd.DataFrame(data)
        self.feature_columns = symptoms
        logging.info("Sample dataset created.")
        return df

    def train_model(self, df: pd.DataFrame, model_type: str = 'random_forest') -> Dict[str, Any]:
        """Train model on dataset"""
        try:
            X = df[self.feature_columns]
            y = df['Disease'] if 'Disease' in df.columns else df[df.columns[-1]]

            # Check feature types
            if not all([np.issubdtype(X[col].dtype, np.number) for col in X.columns]):
                raise ValueError("All features must be numeric. Please clean your data.")

            y_encoded = self.label_encoder.fit_transform(y)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
            )

            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)

            # Initialize model
            if model_type == 'random_forest':
                self.model = RandomForestClassifier(
                    n_estimators=100, max_depth=10, random_state=42, class_weight='balanced'
                )
                X_train_final, X_test_final = X_train, X_test
            else:
                self.model = LogisticRegression(
                    max_iter=1000, random_state=42, class_weight='balanced'
                )
                X_train_final, X_test_final = X_train_scaled, X_test_scaled

            self.model.fit(X_train_final, y_train)
            y_pred = self.model.predict(X_test_final)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

            self.model_metrics = {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'model_type': model_type
            }
            self.is_trained = True
            self._save_model()
            logging.info(f"Model trained. Accuracy: {accuracy:.3f}")
            return self.model_metrics

        except Exception as e:
            logging.error(f"Error training model: {str(e)}")
            return {'error': str(e)}

    def predict(self, symptoms: Dict[str, int]) -> Dict[str, Any]:
        """Make prediction"""
        try:
            if not self.is_trained:
                self._load_model()
            if not self.is_trained:
                return {'error': 'Model not trained'}

            input_data = [symptoms.get(feature, 0) for feature in self.feature_columns]
            input_array = np.array(input_data).reshape(1, -1)

            if isinstance(self.model, LogisticRegression):
                input_array = self.scaler.transform(input_array)

            prediction = self.model.predict(input_array)[0]
            confidence = float(np.max(self.model.predict_proba(input_array)[0])) if hasattr(self.model, 'predict_proba') else 0.8
            predicted_disease = self.label_encoder.inverse_transform([prediction])[0]

            return {
                'disease': predicted_disease,
                'confidence': confidence,
                'success': True
            }

        except Exception as e:
            logging.error(f"Error making prediction: {str(e)}")
            return {'error': str(e), 'success': False}

    def _save_model(self):
        try:
            model_data = {
                'model': self.model,
                'feature_columns': self.feature_columns,
                'label_encoder': self.label_encoder,
                'scaler': self.scaler,
                'metrics': self.model_metrics
            }
            joblib.dump(model_data, 'trained_model.pkl')
            logging.info("Model saved.")
        except Exception as e:
            logging.error(f"Error saving model: {str(e)}")

    def _load_model(self):
        try:
            if os.path.exists('trained_model.pkl'):
                model_data = joblib.load('trained_model.pkl')
                self.model = model_data['model']
                self.feature_columns = model_data['feature_columns']
                self.label_encoder = model_data['label_encoder']
                self.scaler = model_data['scaler']
                self.model_metrics = model_data.get('metrics', {})
                self.is_trained = True
                logging.info("Model loaded.")
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")

    def get_feature_importance(self) -> Dict[str, float]:
        if self.model and hasattr(self.model, 'feature_importances_'):
            return dict(sorted({
                feat: float(imp) for feat, imp in zip(self.feature_columns, self.model.feature_importances_)
            }.items(), key=lambda x: x[1], reverse=True))
        return {}

# Create global predictor instance
predictor = DiseasePredictor()
