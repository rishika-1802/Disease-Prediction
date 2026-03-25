# 🧠 Disease Prediction System

AI-powered disease prediction system that analyzes user symptoms and predicts possible illnesses using Machine Learning models, integrated with a full-stack web application.

---

## 🚀 Tech Stack

![Backend](https://img.shields.io/badge/BACKEND-Flask-4F46E5?style=for-the-badge\&logo=flask\&logoColor=white)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-6366F1?style=for-the-badge\&logo=scikitlearn\&logoColor=white)
![Frontend](https://img.shields.io/badge/FRONTEND-HTML/CSS-7C3AED?style=for-the-badge\&logo=html5\&logoColor=white)
![Database](https://img.shields.io/badge/DATABASE-SQLite-8B5CF6?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Deployment](https://img.shields.io/badge/DEPLOYMENT-Python-A78BFA?style=for-the-badge\&logo=python\&logoColor=white)

---

## 📌 Overview

The **Disease Prediction System** is a full-stack web application that predicts diseases based on symptoms entered by users.

It combines:

* 🧠 Machine Learning models for prediction
* 🌐 Flask backend for handling logic
* 🎨 HTML/CSS frontend for user interaction
* 🗄️ SQLite database for storing data

This system helps in early-stage diagnosis and provides quick, data-driven insights.

---

## 🎯 Features

* 🩺 Symptom-based disease prediction
* 🤖 ML model integration (trained on synthetic dataset)
* 🌐 Web-based interface using Flask
* 📊 Data preprocessing pipeline
* 🗄️ Structured backend with modular architecture
* ⚡ Fast and lightweight execution

---

## 🧠 Machine Learning Models

* Logistic Regression
* Decision Tree
* Random Forest
* Naive Bayes

---

## 📂 Project Structure

📦 Disease-Prediction
 ┣ 📂 instance/                # Database instance
 ┣ 📂 static/                  # CSS, JS, assets
 ┣ 📂 templates/               # HTML templates
 ┣ 📂 utils/                   # Helper functions
 ┣ 📜 app.py                   # Flask app entry
 ┣ 📜 main.py                  # Main execution logic
 ┣ 📜 routes.py                # Route definitions
 ┣ 📜 models.py                # DB models
 ┣ 📜 ml_model.py              # ML model logic
 ┣ 📜 data_processor.py        # Data preprocessing
 ┣ 📜 forms.py                 # Form handling
 ┣ 📜 extensions.py            # Flask extensions
 ┣ 📜 sample_data.py           # Sample inputs
 ┣ 📜 pyproject.toml           # Dependencies/config
 ┗ 📜 README.md
 ┗ 📜 requirements.txt
```

---

## ⚙️ Installation & Setup

```bash id="k3x8dn"
git clone https://github.com/rishika-1802/Disease-Prediction.git
cd Disease-Prediction

pip install -r requirements.txt

python app.py
```

---

## 📊 How It Works

1. User enters symptoms via web interface
2. Data is processed using `data_processor.py`
3. Features are passed to ML model (`ml_model.py`)
4. Model predicts disease
5. Result is displayed on the UI

---

## 📈 Future Improvements

* 🔍 Integrate real medical datasets
* 🌐 Deploy on cloud (Render / AWS)
* 🧑‍⚕️ Doctor consultation recommendation
* 📱 Mobile-friendly UI
* 🧠 Deep Learning model integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the system.

---

