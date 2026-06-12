# Intelligent-Cyber-Threat-Detection-Using-Machine-Learning

## 📌 Project Overview

This project presents an AI-powered Network Intrusion Detection System (IDS) integrated with an interactive Security Operations Center (SOC) Dashboard.

The system leverages Machine Learning algorithms to analyze network traffic and identify malicious activities in real time. Built using the NSL-KDD cybersecurity dataset, the project demonstrates how AI can be applied to modern cyber defense systems.

The dashboard enables security analysts to monitor network activity, analyze threats, visualize attack patterns, and perform intrusion detection through an intuitive web interface.

---

## 🎯 Objectives

- Detect network intrusions using Machine Learning
- Compare multiple classification algorithms
- Identify malicious network traffic with high accuracy
- Visualize cyber threat intelligence through interactive dashboards
- Provide real-time prediction capabilities
- Simulate a Security Operations Center (SOC) environment

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Random Forest
- Decision Tree
- Gradient Boosting
- Logistic Regression

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib
- Seaborn

### Deployment
- Streamlit
- GitHub
- Streamlit Community Cloud

---

## 📂 Dataset

### NSL-KDD Dataset

The NSL-KDD dataset is an improved version of the KDD Cup 1999 dataset and is widely used for evaluating intrusion detection systems.

Dataset contains:

- Normal Traffic
- Denial of Service (DoS)
- Probe Attacks
- User to Root (U2R)
- Remote to Local (R2L)

Source:

https://www.unb.ca/cic/datasets/nsl.html

---

## 📊 Data Preprocessing

The following preprocessing steps were performed:

- Data cleaning
- Feature selection
- Label encoding
- One-hot encoding
- Feature scaling
- Train-test splitting
- Model preparation

Final Dataset Shape:

- Records: 125,973
- Features: 122

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

| Model | Accuracy |
|---------|---------|
| Random Forest | 99.90% |
| Decision Tree | 99.85% |
| Gradient Boosting | 99.62% |
| Logistic Regression | 97.23% |

### Best Performing Model

🏆 Random Forest Classifier

Accuracy: **99.90%**

ROC-AUC: **99.99%**

---

## 📈 Visualizations Included

- Attack Distribution Analysis
- Protocol Distribution
- Top Network Services
- Correlation Heatmap
- Feature Importance Analysis
- Model Accuracy Comparison
- Threat Distribution Charts
- SOC Dashboard Analytics

---

## 🚀 Dashboard Features

### Security Operations Center Dashboard

- Real-Time Intrusion Detection
- Threat Score Gauge
- CSV Traffic Analyzer
- Bulk Threat Scanning
- Attack Classification
- Feature Importance Dashboard
- Model Performance Analytics
- Interactive Visualizations

---

## 📁 Project Structure

```bash
AI-Driven-Network-Intrusion-Detection-and-SOC-Dashboard/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── columns.pkl
├── feature_importance.pkl
├── requirements.txt
├── README.md
│
└── notebooks/
    └── IDS_Model_Training.ipynb
```

---

## ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/AI-Driven-Network-Intrusion-Detection-and-SOC-Dashboard.git
```

Move to project directory

```bash
cd AI-Driven-Network-Intrusion-Detection-and-SOC-Dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit application

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed using:

- GitHub
- Streamlit Community Cloud

Live deployment provides real-time intrusion detection through an interactive browser-based dashboard.

---

## 🔐 Key Cybersecurity Concepts Demonstrated

- Intrusion Detection Systems (IDS)
- Security Operations Center (SOC)
- Threat Intelligence
- Attack Detection
- Network Monitoring
- Cyber Threat Analytics
- Machine Learning Security Applications

---

## 📷 Dashboard Preview

Add screenshots of:

- Home Dashboard
- Threat Detection Screen
- Threat Score Gauge
- CSV Traffic Analyzer
- Feature Importance Visualization

---

## 📚 Future Enhancements

- Deep Learning based IDS
- Real-time packet capture
- SIEM integration
- Live network monitoring
- Threat categorization
- Explainable AI (XAI)
- Cloud deployment pipeline

---

## 👨‍💻 Author

Harsha

Artificial Intelligence & Machine Learning (AIML)

Machine Learning | Cybersecurity | Data Science
https://intelligent-cyber-threat-detection-using-machine-learning-p7it.streamlit.app/

---

## ⭐ Project Highlights

✔ End-to-End Machine Learning Project

✔ Cybersecurity Domain Application

✔ Multiple Model Comparison

✔ Interactive SOC Dashboard

✔ Real-Time Threat Detection

✔ Cloud Deployment

✔ Industry-Relevant Use Case

✔ Resume-Ready Project
