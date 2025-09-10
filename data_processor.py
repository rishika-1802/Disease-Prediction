import pandas as pd
import logging
from typing import List, Dict, Any
import os

class DataProcessor:
    def __init__(self):
        self.dataset_loaded = False
        self.symptoms_list = []
        self.diseases_list = []
        
    def initialize_data(self) -> bool:
        """Initialize data and train model if needed"""
        try:
            from ml_model import predictor
            
            # Load data
            df, success = predictor.load_and_preprocess_data()
            
            if success or not df.empty:
                # Extract symptoms and diseases for UI
                self.symptoms_list = predictor.feature_columns
                
                if 'Disease' in df.columns:
                    self.diseases_list = df['Disease'].unique().tolist()
                else:
                    self.diseases_list = df[df.columns[-1]].unique().tolist()
                
                # Train model if not already trained
                if not predictor.is_trained:
                    if not os.path.exists('trained_model.pkl'):
                        logging.info("Training new model...")
                        metrics = predictor.train_model(df)
                        if 'error' not in metrics:
                            logging.info("Model training completed successfully")
                        else:
                            logging.error(f"Model training failed: {metrics['error']}")
                            return False
                    else:
                        predictor._load_model()
                
                self.dataset_loaded = True
                return True
            else:
                logging.error("Failed to load any data")
                return False
                
        except Exception as e:
            logging.error(f"Error initializing data: {str(e)}")
            return False
    
    def get_symptoms_list(self) -> List[str]:
        """Get list of available symptoms"""
        return self.symptoms_list
    
    def get_diseases_list(self) -> List[str]:
        """Get list of possible diseases"""
        return self.diseases_list
    
    def get_sample_test_cases(self) -> List[Dict[str, Any]]:
        """Get sample test cases for demonstration"""
        return [
            {
                'name': 'Common Cold Symptoms',
                'symptoms': ['fever', 'cough', 'runny_nose', 'sore_throat', 'fatigue'],
                'expected': 'Common Cold'
            },
            {
                'name': 'Flu-like Symptoms',
                'symptoms': ['fever', 'muscle_aches', 'headache', 'fatigue', 'cough'],
                'expected': 'Influenza'
            },
            {
                'name': 'Digestive Issues',
                'symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal_pain', 'fever'],
                'expected': 'Gastroenteritis'
            },
            {
                'name': 'Respiratory Symptoms',
                'symptoms': ['cough', 'shortness_of_breath', 'chest_pain', 'fever'],
                'expected': 'Pneumonia'
            }
        ]

# Global data processor instance
data_processor = DataProcessor()
