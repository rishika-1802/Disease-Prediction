from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import io
import logging
from typing import Dict, Any, List


class PDFReportGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()

    def setup_custom_styles(self):
        """Setup custom paragraph styles for the report"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.blue,
            alignment=1,  # Center alignment
            fontName='Helvetica-Bold'
        ))

        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=20,
            textColor=colors.darkblue,
            fontName='Helvetica-Bold'
        ))

        # Header style
        self.styles.add(ParagraphStyle(
            name='CustomHeader',
            parent=self.styles['Heading3'],
            fontSize=14,
            spaceAfter=15,
            textColor=colors.darkgreen,
            fontName='Helvetica-Bold'
        ))

        # Body style
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=12,
            leading=14,
            fontName='Helvetica'
        ))

        # Emphasis style
        self.styles.add(ParagraphStyle(
            name='CustomEmphasis',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=10,
            textColor=colors.darkred,
            fontName='Helvetica-Bold'
        ))

    def generate_prediction_pdf(self, prediction_data: Dict[str, Any]) -> io.BytesIO:
        """Generate a comprehensive PDF report for disease prediction"""
        try:
            buffer = io.BytesIO()

            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )

            story = []
            story.extend(self._create_header())
            story.extend(self._create_prediction_summary(prediction_data))
            story.extend(self._create_symptoms_analysis(prediction_data))
            story.extend(self._create_confidence_analysis(prediction_data))
            story.extend(self._create_recommendations(prediction_data))
            story.extend(self._create_disclaimer())
            story.extend(self._create_footer())

            doc.build(story)

            buffer.seek(0)
            return buffer

        except Exception as e:
            logging.error(f"Error generating PDF report: {str(e)}")
            raise Exception(f"PDF generation failed: {str(e)}")

    def _create_header(self) -> List:
        story = []
        title = Paragraph("MediPredict - Disease Prediction Report", self.styles['CustomTitle'])
        story.append(title)
        story.append(Spacer(1, 12))

        current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        metadata = f"<b>Report Generated:</b> {current_time}<br/>"
        metadata += f"<b>Report Type:</b> Disease Prediction Analysis<br/>"
        metadata += f"<b>System:</b> MediPredict AI v1.0"

        story.append(Paragraph(metadata, self.styles['CustomBody']))
        story.append(Spacer(1, 20))
        story.append(self._create_line_separator())

        return story

    def _create_prediction_summary(self, prediction_data: Dict[str, Any]) -> List:
        story = []
        story.append(Paragraph("Patient Information", self.styles['CustomSubtitle']))

        patient_data = [
            ['Full Name:', prediction_data.get('name', 'Not provided')],
            ['Age:', f"{prediction_data.get('age', 'Not provided')} years"],
            ['Gender:', prediction_data.get('gender', 'Not provided').title() if prediction_data.get('gender') else 'Not provided'],
            ['Date:', datetime.now().strftime("%B %d, %Y")]
        ]

        patient_table = Table(patient_data, colWidths=[2 * inch, 3 * inch])
        patient_table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('FONT', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.lightgrey, colors.white] * 2),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        story.append(patient_table)
        story.append(Spacer(1, 20))
        story.append(Paragraph("Prediction Results", self.styles['CustomSubtitle']))

        disease = prediction_data.get('disease', 'Unknown')
        confidence = prediction_data.get('confidence', 0)
        confidence_percent = f"{confidence * 100:.1f}%"

        prediction_table_data = [
            ['Predicted Disease', disease],
            ['Confidence Score', confidence_percent],
            ['Prediction Date', datetime.now().strftime("%Y-%m-%d")],
            ['Analysis Method', 'Random Forest Algorithm']
        ]

        prediction_table = Table(prediction_table_data, colWidths=[2.5 * inch, 3 * inch])
        prediction_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('BACKGROUND', (1, 0), (1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        story.append(prediction_table)
        story.append(Spacer(1, 20))

        confidence_interpretation = self._get_confidence_interpretation(confidence)
        story.append(Paragraph(f"<b>Confidence Level Interpretation:</b> {confidence_interpretation}",
                               self.styles['CustomBody']))
        story.append(Spacer(1, 15))

        return story

    def _create_symptoms_analysis(self, prediction_data: Dict[str, Any]) -> List:
        story = []
        story.append(Paragraph("Selected Symptoms Analysis", self.styles['CustomSubtitle']))

        symptoms = prediction_data.get('symptoms', [])
        if symptoms:
            story.append(Paragraph("The following symptoms were analyzed:", self.styles['CustomBody']))
            story.append(Spacer(1, 10))

            symptoms_data = [['Symptom', 'Status']]
            for symptom in symptoms:
                formatted_symptom = symptom.replace('_', ' ').title()
                symptoms_data.append([formatted_symptom, 'Present'])

            symptoms_table = Table(symptoms_data, colWidths=[3 * inch, 1.5 * inch])
            symptoms_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            story.append(symptoms_table)
            story.append(Spacer(1, 15))
            story.append(Paragraph(f"<b>Total Symptoms Reported:</b> {len(symptoms)}", self.styles['CustomBody']))
        else:
            story.append(Paragraph("No symptoms were recorded for this prediction.",
                                   self.styles['CustomBody']))

        story.append(Spacer(1, 20))
        return story

    def _create_confidence_analysis(self, prediction_data: Dict[str, Any]) -> List:
        story = []
        story.append(Paragraph("Confidence Analysis", self.styles['CustomSubtitle']))

        confidence = prediction_data.get('confidence', 0)
        confidence_percent = confidence * 100

        analysis_text = f"""
        The AI model's confidence in this prediction is <b>{confidence_percent:.1f}%</b>. 
        This confidence level is calculated based on how well the selected symptoms 
        match the learned patterns for the predicted disease.
        """

        story.append(Paragraph(analysis_text, self.styles['CustomBody']))
        story.append(Spacer(1, 15))

        if confidence >= 0.8:
            rec_text = "High confidence prediction. The symptoms strongly align with the predicted disease pattern."
            color = colors.darkgreen
        elif confidence >= 0.6:
            rec_text = "Moderate confidence prediction. Consider consulting a healthcare professional for confirmation."
            color = colors.orange
        else:
            rec_text = "Low confidence prediction. Strong recommendation to seek professional medical advice."
            color = colors.red

        story.append(Paragraph(f"<font color='{color.hexval()}'><b>Recommendation:</b> {rec_text}</font>",
                               self.styles['CustomBody']))
        story.append(Spacer(1, 20))

        return story

    def _create_recommendations(self, prediction_data: Dict[str, Any]) -> List:
        story = []
        story.append(Paragraph("Recommendations", self.styles['CustomSubtitle']))

        confidence = prediction_data.get('confidence', 0)

        recommendations = [
            "Consult with a qualified healthcare professional for proper diagnosis",
            "Monitor your symptoms and seek immediate medical attention if they worsen",
            "Follow general health guidelines: rest, proper hydration, and nutrition",
            "Keep a record of symptom changes over time",
            "Do not self-medicate based on this prediction alone"
        ]

        if confidence < 0.6:
            recommendations.insert(0, "Due to low confidence, immediate professional consultation is strongly advised")

        story.append(Paragraph("Based on the prediction analysis, we recommend:", self.styles['CustomBody']))
        story.append(Spacer(1, 10))

        for i, recommendation in enumerate(recommendations, 1):
            story.append(Paragraph(f"{i}. {recommendation}", self.styles['CustomBody']))

        story.append(Spacer(1, 20))

        emergency_text = """
        <font color='red'><b>EMERGENCY WARNING:</b></font><br/>
        Seek immediate medical attention if you experience:
        • Severe chest pain or difficulty breathing
        • Severe bleeding or loss of consciousness
        • Severe allergic reactions
        • Any life-threatening symptoms
        """

        story.append(Paragraph(emergency_text, self.styles['CustomEmphasis']))
        story.append(Spacer(1, 20))

        return story

    def _create_disclaimer(self) -> List:
        story = []
        story.append(Paragraph("Important Medical Disclaimer", self.styles['CustomSubtitle']))

        disclaimer_text = """
        <font color='red'><b>FOR EDUCATIONAL PURPOSES ONLY</b></font><br/><br/>
        This prediction report is generated by an artificial intelligence system and is intended 
        for <b>educational and informational purposes only</b>. It should <b>NEVER</b> be used as a 
        substitute for professional medical advice, diagnosis, or treatment.<br/><br/>
        <b>Important Points:</b><br/>
        • This is NOT a medical diagnosis<br/>
        • Always consult qualified healthcare professionals<br/>
        • The AI model may have limitations and potential errors<br/>
        • Individual medical history and factors are not considered<br/>
        • In case of emergency, contact emergency services immediately<br/><br/>
        By using this system, you acknowledge that you understand these limitations and 
        will seek appropriate professional medical care when needed.
        """

        story.append(Paragraph(disclaimer_text, self.styles['CustomBody']))
        story.append(Spacer(1, 20))
        return story

    def _create_footer(self) -> List:
        story = []
        story.append(self._create_line_separator())
        story.append(Spacer(1, 10))

        footer_text = f"""
        <b>MediPredict AI Disease Prediction System</b><br/>
        Report generated on {datetime.now().strftime("%B %d, %Y at %I:%M %p")}<br/>
        For more information, visit our website or contact support.<br/>
        © 2025 MediPredict. All rights reserved.
        """

        story.append(Paragraph(footer_text, self.styles['CustomBody']))
        return story

    def _create_line_separator(self):
        from reportlab.graphics.shapes import Drawing, Line
        d = Drawing(500, 1)
        d.add(Line(0, 0, 500, 0))
        return d

    def _get_confidence_interpretation(self, confidence: float) -> str:
        if confidence >= 0.9:
            return "Very High - Strong match with known disease patterns"
        elif confidence >= 0.8:
            return "High - Good match with disease symptoms"
        elif confidence >= 0.7:
            return "Moderately High - Reasonable symptom alignment"
        elif confidence >= 0.6:
            return "Moderate - Some symptom alignment, consider professional consultation"
        elif confidence >= 0.5:
            return "Moderate-Low - Limited symptom alignment, professional advice recommended"
        else:
            return "Low - Poor symptom alignment, professional medical consultation strongly advised"


# Global function for easy access
def generate_prediction_pdf(prediction_data: Dict[str, Any]) -> io.BytesIO:
    try:
        generator = PDFReportGenerator()
        return generator.generate_prediction_pdf(prediction_data)
    except Exception as e:
        logging.error(f"Error in generate_prediction_pdf: {str(e)}")
        raise
