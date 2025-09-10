from typing import Dict, Any, List, Optional
import logging

class DiseaseInformationProvider:
    """Provides detailed information about diseases including descriptions, symptoms, and recommendations"""
    
    def __init__(self):
        self.disease_database = self._load_disease_database()
    
    def _load_disease_database(self) -> Dict[str, Dict[str, Any]]:
        """Load comprehensive disease information database"""
        return {
            # Respiratory Diseases
            'Common Cold': {
                'description': 'A viral infection of the upper respiratory tract, typically mild and self-limiting.',
                'common_symptoms': ['runny nose', 'sneezing', 'sore throat', 'mild cough', 'congestion'],
                'severity': 'Low',
                'category': 'Respiratory',
                'recommendations': [
                    'Get plenty of rest and stay hydrated',
                    'Use over-the-counter pain relievers if needed',
                    'Gargle with warm salt water for sore throat',
                    'Use a humidifier to ease congestion',
                    'Avoid close contact with others to prevent spread'
                ],
                'duration': '7-10 days',
                'complications': ['Secondary bacterial infections', 'Sinusitis', 'Ear infections']
            },
            
            'Influenza': {
                'description': 'A contagious respiratory illness caused by influenza viruses, more severe than common cold.',
                'common_symptoms': ['fever', 'muscle aches', 'fatigue', 'cough', 'headache'],
                'severity': 'Medium',
                'category': 'Respiratory',
                'recommendations': [
                    'Get immediate rest and avoid work/school',
                    'Stay well-hydrated with fluids',
                    'Consider antiviral medications if prescribed',
                    'Monitor fever and seek care if very high',
                    'Practice good hygiene to prevent spread'
                ],
                'duration': '1-2 weeks',
                'complications': ['Pneumonia', 'Bronchitis', 'Sinus infections', 'Ear infections']
            },
            
            'COVID-19': {
                'description': 'A respiratory illness caused by SARS-CoV-2 virus, ranging from mild to severe symptoms.',
                'common_symptoms': ['fever', 'cough', 'shortness of breath', 'loss of taste/smell', 'fatigue'],
                'severity': 'Medium',
                'category': 'Respiratory',
                'recommendations': [
                    'Isolate immediately and follow health guidelines',
                    'Monitor oxygen levels and breathing',
                    'Stay hydrated and get plenty of rest',
                    'Seek medical attention if symptoms worsen',
                    'Follow up with healthcare provider'
                ],
                'duration': '2-6 weeks',
                'complications': ['Pneumonia', 'Respiratory failure', 'Multi-organ failure', 'Long COVID']
            },
            
            'Pneumonia': {
                'description': 'An infection that inflames air sacs in one or both lungs, which may fill with fluid.',
                'common_symptoms': ['chest pain', 'cough with phlegm', 'fever', 'shortness of breath', 'fatigue'],
                'severity': 'High',
                'category': 'Respiratory',
                'recommendations': [
                    'Seek immediate medical attention',
                    'Take prescribed antibiotics as directed',
                    'Get plenty of rest and stay hydrated',
                    'Use prescribed respiratory treatments',
                    'Monitor breathing and seek emergency care if worsening'
                ],
                'duration': '1-3 weeks with treatment',
                'complications': ['Respiratory failure', 'Sepsis', 'Lung abscess', 'Pleural effusion']
            },
            
            'Bronchitis': {
                'description': 'Inflammation of the lining of bronchial tubes, often following a cold or respiratory infection.',
                'common_symptoms': ['persistent cough', 'mucus production', 'fatigue', 'chest discomfort', 'mild fever'],
                'severity': 'Medium',
                'category': 'Respiratory',
                'recommendations': [
                    'Rest and avoid irritants like smoke',
                    'Stay well-hydrated to thin mucus',
                    'Use humidifier or breathe steam',
                    'Consider cough suppressants if needed',
                    'See doctor if symptoms persist beyond 3 weeks'
                ],
                'duration': '2-3 weeks',
                'complications': ['Pneumonia', 'Chronic bronchitis']
            },
            
            'Asthma': {
                'description': 'A chronic respiratory condition where airways become inflamed and narrow, making breathing difficult.',
                'common_symptoms': ['wheezing', 'shortness of breath', 'chest tightness', 'coughing', 'difficulty breathing'],
                'severity': 'Medium',
                'category': 'Respiratory',
                'recommendations': [
                    'Use prescribed inhalers as directed',
                    'Identify and avoid triggers',
                    'Monitor peak flow readings regularly',
                    'Have an asthma action plan',
                    'Seek emergency care for severe attacks'
                ],
                'duration': 'Chronic condition',
                'complications': ['Severe asthma attacks', 'Respiratory failure', 'Pneumonia']
            },
            
            # Gastrointestinal Diseases
            'Gastroenteritis': {
                'description': 'Inflammation of the stomach and intestines, commonly called stomach flu.',
                'common_symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal cramps', 'fever'],
                'severity': 'Medium',
                'category': 'Gastrointestinal',
                'recommendations': [
                    'Stay hydrated with clear fluids',
                    'Follow BRAT diet (bananas, rice, applesauce, toast)',
                    'Avoid dairy and fatty foods temporarily',
                    'Rest and avoid solid foods initially',
                    'Seek medical care if severe dehydration occurs'
                ],
                'duration': '3-7 days',
                'complications': ['Dehydration', 'Electrolyte imbalance', 'Kidney problems']
            },
            
            'Food Poisoning': {
                'description': 'Illness caused by consuming contaminated food or water with harmful bacteria, viruses, or toxins.',
                'common_symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal pain', 'fever'],
                'severity': 'Medium',
                'category': 'Gastrointestinal',
                'recommendations': [
                    'Stay hydrated with electrolyte solutions',
                    'Rest and avoid solid foods initially',
                    'Gradually reintroduce bland foods',
                    'Avoid anti-diarrheal medications initially',
                    'Seek medical attention if symptoms are severe'
                ],
                'duration': '1-7 days',
                'complications': ['Severe dehydration', 'Kidney failure', 'Chronic arthritis']
            },
            
            'Acid Reflux': {
                'description': 'A condition where stomach acid flows back into the esophagus, causing irritation.',
                'common_symptoms': ['heartburn', 'acid regurgitation', 'chest pain', 'difficulty swallowing', 'chronic cough'],
                'severity': 'Low',
                'category': 'Gastrointestinal',
                'recommendations': [
                    'Avoid trigger foods (spicy, fatty, acidic)',
                    'Eat smaller, more frequent meals',
                    'Avoid lying down after eating',
                    'Elevate head of bed when sleeping',
                    'Consider over-the-counter antacids'
                ],
                'duration': 'Chronic condition',
                'complications': ['Esophagitis', 'Barrett\'s esophagus', 'Esophageal cancer']
            },
            
            'Irritable Bowel Syndrome': {
                'description': 'A common disorder affecting the large intestine, causing cramping, abdominal pain, and bowel changes.',
                'common_symptoms': ['abdominal pain', 'bloating', 'gas', 'diarrhea or constipation', 'mucus in stool'],
                'severity': 'Medium',
                'category': 'Gastrointestinal',
                'recommendations': [
                    'Identify and avoid trigger foods',
                    'Manage stress through relaxation techniques',
                    'Exercise regularly and maintain routine',
                    'Consider dietary modifications (low FODMAP)',
                    'Work with healthcare provider on treatment plan'
                ],
                'duration': 'Chronic condition',
                'complications': ['Quality of life impact', 'Depression', 'Anxiety']
            },
            
            # Neurological Conditions
            'Migraine': {
                'description': 'A neurological condition characterized by intense, debilitating headaches often accompanied by other symptoms.',
                'common_symptoms': ['severe headache', 'nausea', 'vomiting', 'sensitivity to light', 'sensitivity to sound'],
                'severity': 'Medium',
                'category': 'Neurological',
                'recommendations': [
                    'Rest in a quiet, dark room',
                    'Apply cold or warm compress to head',
                    'Stay hydrated and maintain regular sleep',
                    'Identify and avoid triggers',
                    'Consider prescribed migraine medications'
                ],
                'duration': '4-72 hours per episode',
                'complications': ['Chronic daily headache', 'Medication overuse headache', 'Status migrainosus']
            },
            
            'Tension Headache': {
                'description': 'The most common type of headache, often related to stress, muscle tension, or fatigue.',
                'common_symptoms': ['dull, aching head pain', 'pressure around forehead', 'tender scalp', 'neck/shoulder tension'],
                'severity': 'Low',
                'category': 'Neurological',
                'recommendations': [
                    'Practice stress management techniques',
                    'Maintain regular sleep schedule',
                    'Stay hydrated and eat regular meals',
                    'Use over-the-counter pain relievers as needed',
                    'Apply heat or cold to head and neck'
                ],
                'duration': '30 minutes to several hours',
                'complications': ['Chronic tension headaches', 'Medication overuse']
            },
            
            # Musculoskeletal Conditions
            'Arthritis': {
                'description': 'Inflammation of one or more joints, causing pain, swelling, and reduced range of motion.',
                'common_symptoms': ['joint pain', 'swelling', 'stiffness', 'reduced range of motion', 'fatigue'],
                'severity': 'Medium',
                'category': 'Musculoskeletal',
                'recommendations': [
                    'Maintain regular, low-impact exercise',
                    'Apply heat/cold therapy as needed',
                    'Maintain healthy weight',
                    'Use prescribed medications as directed',
                    'Consider physical therapy'
                ],
                'duration': 'Chronic condition',
                'complications': ['Joint deformity', 'Disability', 'Heart problems', 'Lung problems']
            },
            
            'Back Pain': {
                'description': 'Pain in the back that can range from muscle aching to shooting, burning, or stabbing sensation.',
                'common_symptoms': ['lower back pain', 'muscle spasms', 'limited flexibility', 'pain radiating to legs'],
                'severity': 'Medium',
                'category': 'Musculoskeletal',
                'recommendations': [
                    'Apply ice for acute pain, heat for chronic pain',
                    'Maintain good posture and ergonomics',
                    'Exercise regularly to strengthen core muscles',
                    'Avoid prolonged bed rest',
                    'Consider physical therapy if pain persists'
                ],
                'duration': 'Variable - acute to chronic',
                'complications': ['Chronic pain', 'Nerve damage', 'Disability']
            },
            
            # Cardiovascular Conditions
            'Hypertension': {
                'description': 'High blood pressure, often called the "silent killer" as it usually has no symptoms.',
                'common_symptoms': ['often no symptoms', 'headaches', 'shortness of breath', 'chest pain', 'dizziness'],
                'severity': 'High',
                'category': 'Cardiovascular',
                'recommendations': [
                    'Monitor blood pressure regularly',
                    'Maintain healthy diet low in sodium',
                    'Exercise regularly and maintain healthy weight',
                    'Limit alcohol and quit smoking',
                    'Take prescribed medications as directed'
                ],
                'duration': 'Chronic condition',
                'complications': ['Heart attack', 'Stroke', 'Kidney disease', 'Heart failure']
            },
            
            # Metabolic Conditions
            'Diabetes': {
                'description': 'A group of metabolic disorders characterized by high blood sugar levels.',
                'common_symptoms': ['frequent urination', 'excessive thirst', 'unexplained weight loss', 'fatigue', 'blurred vision'],
                'severity': 'High',
                'category': 'Metabolic',
                'recommendations': [
                    'Monitor blood glucose levels regularly',
                    'Follow prescribed diet and meal planning',
                    'Exercise regularly as approved by doctor',
                    'Take medications/insulin as prescribed',
                    'Regular medical check-ups and screenings'
                ],
                'duration': 'Chronic condition',
                'complications': ['Heart disease', 'Kidney disease', 'Eye problems', 'Nerve damage']
            },
            
            # Infectious Diseases
            'Urinary Tract Infection': {
                'description': 'An infection in any part of the urinary system, most commonly affecting the bladder.',
                'common_symptoms': ['burning urination', 'frequent urination', 'cloudy urine', 'pelvic pain', 'strong-smelling urine'],
                'severity': 'Medium',
                'category': 'Infectious',
                'recommendations': [
                    'Drink plenty of water to flush bacteria',
                    'Take prescribed antibiotics completely',
                    'Urinate frequently and after intercourse',
                    'Avoid irritating products',
                    'Seek medical attention if symptoms worsen'
                ],
                'duration': '3-7 days with treatment',
                'complications': ['Kidney infection', 'Recurrent infections', 'Sepsis']
            },
            
            'Sinusitis': {
                'description': 'Inflammation or swelling of the tissue lining the sinuses, often following a cold.',
                'common_symptoms': ['facial pain and pressure', 'nasal congestion', 'thick nasal discharge', 'reduced sense of smell', 'cough'],
                'severity': 'Medium',
                'category': 'Respiratory',
                'recommendations': [
                    'Use saline nasal irrigation',
                    'Apply warm compresses to face',
                    'Stay hydrated and use humidifier',
                    'Consider decongestants for short-term relief',
                    'See doctor if symptoms persist beyond 10 days'
                ],
                'duration': '2-4 weeks',
                'complications': ['Chronic sinusitis', 'Meningitis', 'Brain abscess']
            },
            
            'Allergic Rhinitis': {
                'description': 'An allergic response to airborne allergens, commonly known as hay fever.',
                'common_symptoms': ['sneezing', 'runny nose', 'itchy eyes', 'nasal congestion', 'postnasal drip'],
                'severity': 'Low',
                'category': 'Allergic',
                'recommendations': [
                    'Identify and avoid allergen triggers',
                    'Use air purifiers and keep windows closed',
                    'Consider antihistamines for symptom relief',
                    'Nasal corticosteroid sprays may help',
                    'Regular cleaning to reduce allergens'
                ],
                'duration': 'Seasonal or year-round',
                'complications': ['Sinusitis', 'Ear infections', 'Sleep problems']
            },
            
            # Mental Health Conditions
            'Anxiety Disorder': {
                'description': 'A mental health condition characterized by excessive worry, fear, or nervousness.',
                'common_symptoms': ['excessive worry', 'restlessness', 'fatigue', 'difficulty concentrating', 'muscle tension'],
                'severity': 'Medium',
                'category': 'Mental Health',
                'recommendations': [
                    'Practice relaxation and breathing techniques',
                    'Regular exercise and healthy lifestyle',
                    'Consider therapy or counseling',
                    'Limit caffeine and alcohol',
                    'Seek professional mental health support'
                ],
                'duration': 'Variable - can be chronic',
                'complications': ['Depression', 'Substance abuse', 'Social isolation']
            },
            
            'Depression': {
                'description': 'A mood disorder causing persistent feelings of sadness and loss of interest in activities.',
                'common_symptoms': ['persistent sadness', 'loss of interest', 'fatigue', 'sleep changes', 'appetite changes'],
                'severity': 'High',
                'category': 'Mental Health',
                'recommendations': [
                    'Seek professional mental health treatment',
                    'Consider therapy and/or medication',
                    'Maintain social connections',
                    'Regular exercise and healthy routine',
                    'Crisis support if having suicidal thoughts'
                ],
                'duration': 'Variable - can be chronic',
                'complications': ['Suicide risk', 'Substance abuse', 'Physical health problems']
            },
            
            'Insomnia': {
                'description': 'A sleep disorder characterized by difficulty falling asleep, staying asleep, or getting quality sleep.',
                'common_symptoms': ['difficulty falling asleep', 'frequent awakening', 'early morning awakening', 'daytime fatigue', 'irritability'],
                'severity': 'Medium',
                'category': 'Sleep Disorder',
                'recommendations': [
                    'Maintain consistent sleep schedule',
                    'Create comfortable sleep environment',
                    'Avoid caffeine and screens before bedtime',
                    'Practice relaxation techniques',
                    'Consider cognitive behavioral therapy for insomnia'
                ],
                'duration': 'Variable - acute to chronic',
                'complications': ['Chronic fatigue', 'Depression', 'Impaired performance', 'Increased accident risk']
            }
        }
    
    def get_disease_info(self, disease_name: str) -> Optional[Dict[str, Any]]:
        """Get comprehensive information about a specific disease
        
        Args:
            disease_name: Name of the disease to look up
            
        Returns:
            Dictionary containing disease information or None if not found
        """
        try:
            # Normalize disease name for lookup
            normalized_name = self._normalize_disease_name(disease_name)
            
            # Try exact match first
            if normalized_name in self.disease_database:
                return self.disease_database[normalized_name]
            
            # Try fuzzy matching
            for disease in self.disease_database.keys():
                if normalized_name.lower() in disease.lower() or disease.lower() in normalized_name.lower():
                    return self.disease_database[disease]
            
            # If no match found, return generic information
            return self._get_generic_disease_info(disease_name)
            
        except Exception as e:
            logging.error(f"Error retrieving disease info for {disease_name}: {str(e)}")
            return self._get_generic_disease_info(disease_name)
    
    def _normalize_disease_name(self, disease_name: str) -> str:
        """Normalize disease name for consistent lookup"""
        # Remove extra spaces and convert to title case
        return ' '.join(disease_name.strip().split()).title()
    
    def _get_generic_disease_info(self, disease_name: str) -> Dict[str, Any]:
        """Return generic disease information when specific info is not available"""
        return {
            'description': f'{disease_name} is a medical condition that requires professional evaluation and diagnosis.',
            'common_symptoms': ['Symptoms vary depending on the specific condition'],
            'severity': 'Unknown',
            'category': 'Medical Condition',
            'recommendations': [
                'Consult with a qualified healthcare professional for proper diagnosis',
                'Monitor symptoms and seek medical attention if they worsen',
                'Follow general health guidelines: rest, hydration, and proper nutrition',
                'Do not attempt self-diagnosis or self-treatment',
                'Keep a record of symptoms to discuss with your healthcare provider'
            ],
            'duration': 'Variable',
            'complications': ['Complications depend on the specific condition and individual factors']
        }
    
    def get_diseases_by_category(self, category: str) -> List[str]:
        """Get all diseases in a specific category
        
        Args:
            category: Medical category to filter by
            
        Returns:
            List of disease names in the specified category
        """
        try:
            diseases = []
            for disease_name, info in self.disease_database.items():
                if info.get('category', '').lower() == category.lower():
                    diseases.append(disease_name)
            return diseases
        except Exception as e:
            logging.error(f"Error retrieving diseases by category {category}: {str(e)}")
            return []
    
    def get_all_categories(self) -> List[str]:
        """Get all available disease categories
        
        Returns:
            List of unique category names
        """
        try:
            categories = set()
            for info in self.disease_database.values():
                category = info.get('category')
                if category:
                    categories.add(category)
            return sorted(list(categories))
        except Exception as e:
            logging.error(f"Error retrieving categories: {str(e)}")
            return []
    
    def search_diseases(self, query: str) -> List[Dict[str, Any]]:
        """Search for diseases based on symptoms or names
        
        Args:
            query: Search query (disease name or symptom)
            
        Returns:
            List of matching diseases with their information
        """
        try:
            results = []
            query_lower = query.lower()
            
            for disease_name, info in self.disease_database.items():
                # Check disease name
                if query_lower in disease_name.lower():
                    results.append({
                        'name': disease_name,
                        'info': info,
                        'match_type': 'name'
                    })
                    continue
                
                # Check symptoms
                symptoms = info.get('common_symptoms', [])
                if any(query_lower in symptom.lower() for symptom in symptoms):
                    results.append({
                        'name': disease_name,
                        'info': info,
                        'match_type': 'symptom'
                    })
                    continue
                
                # Check description
                description = info.get('description', '')
                if query_lower in description.lower():
                    results.append({
                        'name': disease_name,
                        'info': info,
                        'match_type': 'description'
                    })
            
            return results
            
        except Exception as e:
            logging.error(f"Error searching diseases with query '{query}': {str(e)}")
            return []

# Global instance for easy access
disease_info_provider = DiseaseInformationProvider()

def get_disease_info(disease_name: str) -> Optional[Dict[str, Any]]:
    """Global function to get disease information
    
    Args:
        disease_name: Name of the disease
        
    Returns:
        Disease information dictionary or None
    """
    return disease_info_provider.get_disease_info(disease_name)

def search_diseases_by_symptom(symptom: str) -> List[Dict[str, Any]]:
    """Search for diseases that commonly present with a specific symptom
    
    Args:
        symptom: Symptom to search for
        
    Returns:
        List of diseases that commonly have this symptom
    """
    return disease_info_provider.search_diseases(symptom)

def get_disease_categories() -> List[str]:
    """Get all available disease categories
    
    Returns:
        List of category names
    """
    return disease_info_provider.get_all_categories()
