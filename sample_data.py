"""
Sample data generator for MediPredict disease prediction system.
Creates realistic synthetic medical data when the actual dataset is not available.
"""

import pandas as pd
import numpy as np
import random
from typing import Dict, List, Tuple
import logging

class MedicalDataGenerator:
    """Generates realistic synthetic medical data for training and testing"""
    
    def __init__(self, random_seed: int = 42):
        """Initialize the data generator with a random seed for reproducibility"""
        np.random.seed(random_seed)
        random.seed(random_seed)
        
        # Define comprehensive symptom categories and relationships
        self.symptoms = {
            'respiratory': [
                'cough', 'shortness_of_breath', 'chest_pain', 'wheezing',
                'sore_throat', 'runny_nose', 'nasal_congestion', 'sneezing'
            ],
            'gastrointestinal': [
                'nausea', 'vomiting', 'diarrhea', 'constipation', 'abdominal_pain',
                'bloating', 'loss_of_appetite', 'heartburn', 'difficulty_swallowing'
            ],
            'neurological': [
                'headache', 'dizziness', 'confusion', 'memory_problems',
                'blurred_vision', 'numbness', 'tingling', 'seizures'
            ],
            'systemic': [
                'fever', 'fatigue', 'weight_loss', 'weight_gain', 'night_sweats',
                'chills', 'weakness', 'loss_of_energy'
            ],
            'musculoskeletal': [
                'joint_pain', 'muscle_aches', 'back_pain', 'neck_pain',
                'stiffness', 'swelling', 'reduced_mobility'
            ],
            'dermatological': [
                'rash', 'itching', 'skin_discoloration', 'dry_skin',
                'hair_loss', 'nail_changes'
            ],
            'cardiovascular': [
                'palpitations', 'irregular_heartbeat', 'chest_tightness',
                'leg_swelling', 'cold_extremities'
            ],
            'genitourinary': [
                'frequent_urination', 'painful_urination', 'blood_in_urine',
                'excessive_thirst', 'kidney_pain'
            ],
            'psychiatric': [
                'anxiety', 'depression', 'mood_changes', 'sleep_disturbances',
                'irritability', 'concentration_problems'
            ]
        }
        
        # Flatten all symptoms into a single list
        self.all_symptoms = []
        for category_symptoms in self.symptoms.values():
            self.all_symptoms.extend(category_symptoms)
        
        # Define diseases with their typical symptom patterns
        self.disease_patterns = self._define_disease_patterns()
        
        logging.info(f"Initialized data generator with {len(self.all_symptoms)} symptoms and {len(self.disease_patterns)} diseases")
    
    def _define_disease_patterns(self) -> Dict[str, Dict]:
        """Define realistic disease patterns with associated symptoms and probabilities"""
        return {
            # Respiratory Diseases
            'Common Cold': {
                'primary_symptoms': ['runny_nose', 'sore_throat', 'cough', 'sneezing'],
                'secondary_symptoms': ['nasal_congestion', 'headache', 'fatigue'],
                'primary_prob': 0.8,
                'secondary_prob': 0.4,
                'category': 'respiratory'
            },
            'Influenza': {
                'primary_symptoms': ['fever', 'muscle_aches', 'fatigue', 'cough'],
                'secondary_symptoms': ['headache', 'sore_throat', 'chills', 'weakness'],
                'primary_prob': 0.85,
                'secondary_prob': 0.5,
                'category': 'respiratory'
            },
            'COVID-19': {
                'primary_symptoms': ['fever', 'cough', 'shortness_of_breath', 'fatigue'],
                'secondary_symptoms': ['headache', 'muscle_aches', 'loss_of_appetite', 'confusion'],
                'primary_prob': 0.75,
                'secondary_prob': 0.4,
                'category': 'respiratory'
            },
            'Pneumonia': {
                'primary_symptoms': ['chest_pain', 'cough', 'fever', 'shortness_of_breath'],
                'secondary_symptoms': ['fatigue', 'chills', 'confusion', 'weakness'],
                'primary_prob': 0.9,
                'secondary_prob': 0.6,
                'category': 'respiratory'
            },
            'Bronchitis': {
                'primary_symptoms': ['cough', 'chest_pain', 'fatigue'],
                'secondary_symptoms': ['fever', 'shortness_of_breath', 'wheezing'],
                'primary_prob': 0.85,
                'secondary_prob': 0.3,
                'category': 'respiratory'
            },
            'Asthma': {
                'primary_symptoms': ['wheezing', 'shortness_of_breath', 'chest_tightness', 'cough'],
                'secondary_symptoms': ['anxiety', 'fatigue', 'difficulty_swallowing'],
                'primary_prob': 0.9,
                'secondary_prob': 0.2,
                'category': 'respiratory'
            },
            'Sinusitis': {
                'primary_symptoms': ['nasal_congestion', 'headache', 'runny_nose'],
                'secondary_symptoms': ['fever', 'cough', 'fatigue', 'dizziness'],
                'primary_prob': 0.8,
                'secondary_prob': 0.3,
                'category': 'respiratory'
            },
            'Allergic Rhinitis': {
                'primary_symptoms': ['sneezing', 'runny_nose', 'nasal_congestion'],
                'secondary_symptoms': ['headache', 'fatigue', 'irritability'],
                'primary_prob': 0.85,
                'secondary_prob': 0.25,
                'category': 'respiratory'
            },
            
            # Gastrointestinal Diseases
            'Gastroenteritis': {
                'primary_symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal_pain'],
                'secondary_symptoms': ['fever', 'fatigue', 'loss_of_appetite', 'weakness'],
                'primary_prob': 0.85,
                'secondary_prob': 0.5,
                'category': 'gastrointestinal'
            },
            'Food Poisoning': {
                'primary_symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal_pain'],
                'secondary_symptoms': ['fever', 'chills', 'weakness', 'headache'],
                'primary_prob': 0.9,
                'secondary_prob': 0.4,
                'category': 'gastrointestinal'
            },
            'Acid Reflux': {
                'primary_symptoms': ['heartburn', 'chest_pain', 'difficulty_swallowing'],
                'secondary_symptoms': ['cough', 'sore_throat', 'nausea'],
                'primary_prob': 0.8,
                'secondary_prob': 0.3,
                'category': 'gastrointestinal'
            },
            'Irritable Bowel Syndrome': {
                'primary_symptoms': ['abdominal_pain', 'bloating', 'diarrhea', 'constipation'],
                'secondary_symptoms': ['fatigue', 'anxiety', 'mood_changes'],
                'primary_prob': 0.75,
                'secondary_prob': 0.4,
                'category': 'gastrointestinal'
            },
            'Peptic Ulcer': {
                'primary_symptoms': ['abdominal_pain', 'nausea', 'loss_of_appetite'],
                'secondary_symptoms': ['vomiting', 'weight_loss', 'fatigue'],
                'primary_prob': 0.8,
                'secondary_prob': 0.3,
                'category': 'gastrointestinal'
            },
            
            # Neurological Conditions
            'Migraine': {
                'primary_symptoms': ['headache', 'nausea', 'blurred_vision'],
                'secondary_symptoms': ['vomiting', 'dizziness', 'fatigue', 'mood_changes'],
                'primary_prob': 0.9,
                'secondary_prob': 0.5,
                'category': 'neurological'
            },
            'Tension Headache': {
                'primary_symptoms': ['headache', 'muscle_aches', 'fatigue'],
                'secondary_symptoms': ['neck_pain', 'irritability', 'concentration_problems'],
                'primary_prob': 0.85,
                'secondary_prob': 0.4,
                'category': 'neurological'
            },
            'Vertigo': {
                'primary_symptoms': ['dizziness', 'nausea', 'balance_problems'],
                'secondary_symptoms': ['vomiting', 'headache', 'anxiety'],
                'primary_prob': 0.9,
                'secondary_prob': 0.3,
                'category': 'neurological'
            },
            
            # Musculoskeletal Conditions
            'Arthritis': {
                'primary_symptoms': ['joint_pain', 'stiffness', 'swelling'],
                'secondary_symptoms': ['fatigue', 'reduced_mobility', 'muscle_aches'],
                'primary_prob': 0.85,
                'secondary_prob': 0.5,
                'category': 'musculoskeletal'
            },
            'Back Pain': {
                'primary_symptoms': ['back_pain', 'muscle_aches', 'stiffness'],
                'secondary_symptoms': ['numbness', 'tingling', 'reduced_mobility'],
                'primary_prob': 0.9,
                'secondary_prob': 0.3,
                'category': 'musculoskeletal'
            },
            'Fibromyalgia': {
                'primary_symptoms': ['muscle_aches', 'fatigue', 'joint_pain'],
                'secondary_symptoms': ['sleep_disturbances', 'depression', 'concentration_problems'],
                'primary_prob': 0.8,
                'secondary_prob': 0.6,
                'category': 'musculoskeletal'
            },
            
            # Cardiovascular Conditions
            'Hypertension': {
                'primary_symptoms': ['headache', 'dizziness', 'chest_pain'],
                'secondary_symptoms': ['shortness_of_breath', 'palpitations', 'fatigue'],
                'primary_prob': 0.6,  # Often asymptomatic
                'secondary_prob': 0.3,
                'category': 'cardiovascular'
            },
            'Heart Palpitations': {
                'primary_symptoms': ['palpitations', 'irregular_heartbeat', 'chest_tightness'],
                'secondary_symptoms': ['anxiety', 'dizziness', 'shortness_of_breath'],
                'primary_prob': 0.9,
                'secondary_prob': 0.4,
                'category': 'cardiovascular'
            },
            
            # Metabolic Conditions
            'Diabetes': {
                'primary_symptoms': ['frequent_urination', 'excessive_thirst', 'fatigue'],
                'secondary_symptoms': ['weight_loss', 'blurred_vision', 'weakness'],
                'primary_prob': 0.8,
                'secondary_prob': 0.5,
                'category': 'metabolic'
            },
            'Hyperthyroidism': {
                'primary_symptoms': ['weight_loss', 'palpitations', 'anxiety'],
                'secondary_symptoms': ['fatigue', 'irritability', 'sleep_disturbances'],
                'primary_prob': 0.8,
                'secondary_prob': 0.4,
                'category': 'metabolic'
            },
            'Hypothyroidism': {
                'primary_symptoms': ['weight_gain', 'fatigue', 'cold_extremities'],
                'secondary_symptoms': ['depression', 'dry_skin', 'concentration_problems'],
                'primary_prob': 0.75,
                'secondary_prob': 0.5,
                'category': 'metabolic'
            },
            
            # Infectious Diseases
            'Urinary Tract Infection': {
                'primary_symptoms': ['painful_urination', 'frequent_urination', 'kidney_pain'],
                'secondary_symptoms': ['fever', 'nausea', 'fatigue'],
                'primary_prob': 0.9,
                'secondary_prob': 0.4,
                'category': 'infectious'
            },
            'Mononucleosis': {
                'primary_symptoms': ['sore_throat', 'fever', 'swelling', 'fatigue'],
                'secondary_symptoms': ['headache', 'muscle_aches', 'loss_of_appetite'],
                'primary_prob': 0.85,
                'secondary_prob': 0.5,
                'category': 'infectious'
            },
            
            # Dermatological Conditions
            'Eczema': {
                'primary_symptoms': ['rash', 'itching', 'dry_skin'],
                'secondary_symptoms': ['skin_discoloration', 'irritability', 'sleep_disturbances'],
                'primary_prob': 0.9,
                'secondary_prob': 0.3,
                'category': 'dermatological'
            },
            'Psoriasis': {
                'primary_symptoms': ['rash', 'skin_discoloration', 'itching'],
                'secondary_symptoms': ['joint_pain', 'nail_changes', 'fatigue'],
                'primary_prob': 0.85,
                'secondary_prob': 0.4,
                'category': 'dermatological'
            },
            
            # Mental Health Conditions
            'Anxiety Disorder': {
                'primary_symptoms': ['anxiety', 'palpitations', 'muscle_aches'],
                'secondary_symptoms': ['sleep_disturbances', 'concentration_problems', 'fatigue'],
                'primary_prob': 0.8,
                'secondary_prob': 0.6,
                'category': 'psychiatric'
            },
            'Depression': {
                'primary_symptoms': ['depression', 'fatigue', 'loss_of_appetite'],
                'secondary_symptoms': ['sleep_disturbances', 'concentration_problems', 'weight_loss'],
                'primary_prob': 0.85,
                'secondary_prob': 0.5,
                'category': 'psychiatric'
            },
            'Insomnia': {
                'primary_symptoms': ['sleep_disturbances', 'fatigue', 'irritability'],
                'secondary_symptoms': ['concentration_problems', 'headache', 'anxiety'],
                'primary_prob': 0.9,
                'secondary_prob': 0.4,
                'category': 'psychiatric'
            }
        }
    
    def generate_dataset(self, num_samples: int = 5000) -> pd.DataFrame:
        """Generate a comprehensive synthetic medical dataset
        
        Args:
            num_samples: Number of patient records to generate
            
        Returns:
            DataFrame with symptoms as columns and disease as target
        """
        logging.info(f"Generating synthetic dataset with {num_samples} samples")
        
        # Initialize the dataset
        data = []
        diseases = list(self.disease_patterns.keys())
        
        # Generate samples with realistic disease distribution
        disease_weights = self._calculate_disease_weights()
        
        for i in range(num_samples):
            # Select a disease based on realistic prevalence
            disease = np.random.choice(diseases, p=disease_weights)
            
            # Generate symptoms for this disease
            sample = self._generate_patient_symptoms(disease)
            sample['Disease'] = disease
            
            data.append(sample)
            
            if (i + 1) % 1000 == 0:
                logging.info(f"Generated {i + 1}/{num_samples} samples")
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Ensure all symptom columns are present (fill missing with 0)
        for symptom in self.all_symptoms:
            if symptom not in df.columns:
                df[symptom] = 0
        
        # Reorder columns (symptoms first, then disease)
        symptom_columns = sorted([col for col in df.columns if col != 'Disease'])
        df = df[symptom_columns + ['Disease']]
        
        logging.info(f"Dataset generated successfully: {df.shape[0]} rows, {df.shape[1]} columns")
        logging.info(f"Disease distribution:\n{df['Disease'].value_counts()}")
        
        return df
    
    def _calculate_disease_weights(self) -> np.ndarray:
        """Calculate realistic disease prevalence weights"""
        diseases = list(self.disease_patterns.keys())
        weights = []
        
        # Define prevalence categories
        high_prevalence = ['Common Cold', 'Tension Headache', 'Back Pain', 'Anxiety Disorder']
        medium_prevalence = ['Influenza', 'Gastroenteritis', 'Migraine', 'Hypertension', 'Arthritis']
        low_prevalence = ['Pneumonia', 'COVID-19', 'Diabetes', 'Depression']
        
        for disease in diseases:
            if disease in high_prevalence:
                weights.append(3.0)  # High prevalence
            elif disease in medium_prevalence:
                weights.append(2.0)  # Medium prevalence
            elif disease in low_prevalence:
                weights.append(1.5)  # Lower but still significant
            else:
                weights.append(1.0)  # Base prevalence
        
        # Normalize weights to probabilities
        weights = np.array(weights)
        return weights / weights.sum()
    
    def _generate_patient_symptoms(self, disease: str) -> Dict[str, int]:
        """Generate realistic symptom pattern for a specific disease
        
        Args:
            disease: Name of the disease
            
        Returns:
            Dictionary with symptom names as keys and 0/1 as values
        """
        pattern = self.disease_patterns[disease]
        symptoms = {}
        
        # Initialize all symptoms to 0
        for symptom in self.all_symptoms:
            symptoms[symptom] = 0
        
        # Add primary symptoms with high probability
        for symptom in pattern['primary_symptoms']:
            if symptom in self.all_symptoms and np.random.random() < pattern['primary_prob']:
                symptoms[symptom] = 1
        
        # Add secondary symptoms with lower probability
        for symptom in pattern['secondary_symptoms']:
            if symptom in self.all_symptoms and np.random.random() < pattern['secondary_prob']:
                symptoms[symptom] = 1
        
        # Add some noise - random symptoms with very low probability
        noise_symptoms = [s for s in self.all_symptoms 
                         if s not in pattern['primary_symptoms'] + pattern['secondary_symptoms']]
        
        for symptom in noise_symptoms:
            if np.random.random() < 0.05:  # 5% chance of random symptom
                symptoms[symptom] = 1
        
        # Ensure at least one symptom is present
        if sum(symptoms.values()) == 0:
            # Add a random primary symptom
            random_primary = np.random.choice(pattern['primary_symptoms'])
            if random_primary in symptoms:
                symptoms[random_primary] = 1
        
        return symptoms
    
    def generate_test_cases(self) -> List[Dict[str, any]]:
        """Generate specific test cases for demonstration"""
        test_cases = []
        
        # Create targeted test cases for major disease categories
        for disease, pattern in list(self.disease_patterns.items())[:10]:  # First 10 diseases
            symptoms = []
            
            # Add all primary symptoms for clear cases
            for symptom in pattern['primary_symptoms']:
                if symptom in self.all_symptoms:
                    symptoms.append(symptom)
            
            # Add some secondary symptoms
            for symptom in pattern['secondary_symptoms'][:2]:  # Max 2 secondary
                if symptom in self.all_symptoms:
                    symptoms.append(symptom)
            
            test_cases.append({
                'name': f'{disease} Test Case',
                'symptoms': symptoms,
                'expected_disease': disease,
                'description': f'Typical presentation of {disease}'
            })
        
        return test_cases
    
    def get_disease_statistics(self) -> Dict[str, any]:
        """Get statistics about the disease patterns"""
        stats = {
            'total_diseases': len(self.disease_patterns),
            'total_symptoms': len(self.all_symptoms),
            'symptom_categories': {cat: len(symptoms) for cat, symptoms in self.symptoms.items()},
            'disease_categories': {}
        }
        
        # Count diseases by category
        for disease, pattern in self.disease_patterns.items():
            category = pattern.get('category', 'unknown')
            if category not in stats['disease_categories']:
                stats['disease_categories'][category] = 0
            stats['disease_categories'][category] += 1
        
        return stats
    
    def save_dataset(self, df: pd.DataFrame, filename: str = 'synthetic_medical_dataset.xlsx'):
        """Save the generated dataset to an Excel file
        
        Args:
            df: DataFrame to save
            filename: Output filename
        """
        try:
            df.to_excel(filename, index=False)
            logging.info(f"Dataset saved to {filename}")
        except Exception as e:
            logging.error(f"Failed to save dataset: {str(e)}")
            # Fallback to CSV
            csv_filename = filename.replace('.xlsx', '.csv')
            df.to_csv(csv_filename, index=False)
            logging.info(f"Dataset saved to {csv_filename} (CSV format)")

def create_sample_dataset(num_samples: int = 5000, filename: str = None) -> pd.DataFrame:
    """Convenience function to create and optionally save a sample dataset
    
    Args:
        num_samples: Number of samples to generate
        filename: Optional filename to save the dataset
        
    Returns:
        Generated DataFrame
    """
    generator = MedicalDataGenerator()
    df = generator.generate_dataset(num_samples)
    
    if filename:
        generator.save_dataset(df, filename)
    
    return df

def get_sample_test_cases() -> List[Dict[str, any]]:
    """Get sample test cases for demonstration
    
    Returns:
        List of test case dictionaries
    """
    generator = MedicalDataGenerator()
    return generator.generate_test_cases()

def get_dataset_statistics() -> Dict[str, any]:
    """Get statistics about the synthetic dataset structure
    
    Returns:
        Dictionary with dataset statistics
    """
    generator = MedicalDataGenerator()
    return generator.get_disease_statistics()

# Example usage and testing
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Create a sample dataset
    print("Creating synthetic medical dataset...")
    
    generator = MedicalDataGenerator()
    
    # Generate dataset
    df = generator.generate_dataset(1000)
    
    # Display basic information
    print(f"\nDataset shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nDisease distribution:")
    print(df['Disease'].value_counts())
    
    # Show sample rows
    print(f"\nSample data:")
    print(df.head())
    
    # Get statistics
    stats = generator.get_disease_statistics()
    print(f"\nDataset statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Generate test cases
    test_cases = generator.generate_test_cases()
    print(f"\nGenerated {len(test_cases)} test cases")
    
    # Save dataset
    try:
        generator.save_dataset(df, 'synthetic_symptoms_dataset_realistic_100_diseases.xlsx')
        print("Dataset saved successfully!")
    except Exception as e:
        print(f"Error saving dataset: {e}")
