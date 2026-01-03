# 📱 SMS Spam Detection using Machine Learning

## 📌 Overview
This project builds a machine learning system to classify SMS messages as **Spam** or **Ham (Not Spam)**.  
The project is designed with **real-world deployment** in mind and demonstrates an end-to-end ML workflow.

A public web app is deployed using **Streamlit** for live testing.

---

## 📊 Dataset
- **Source:** UCI Machine Learning Repository – SMS Spam Collection
- **Total messages:** 5,572
- **Classes:**
  - Ham: 4,825
  - Spam: 747

This dataset closely matches real-world SMS messages, making it suitable for deployment.

---

## 🛠️ Approach

### 1. Exploratory Data Analysis
- Class distribution analysis
- Message length analysis
- Spam vs Ham characteristics

### 2. Text Preprocessing
- Lowercasing
- Removal of URLs and special characters
- Minimal cleaning to preserve semantic meaning

### 3. Feature Engineering
- TF-IDF Vectorization
- Unigrams and bigrams
- Vocabulary size control

### 4. Modeling
- Logistic Regression with class balancing
- Threshold tuning to reduce missed spam messages

### 5. Evaluation
- Confusion matrix
- Precision, Recall, F1-score
- Precision–Recall tradeoff analysis

---

## 📈 Results
- **Accuracy:** ~98%
- **Spam Recall:** ~95%
- **Balanced false positives and false negatives**
- Stable and realistic behavior during deployment testing

---

## 🚀 Deployment
The model is deployed as a public web application using **Streamlit**.

🔗 **Live App:** *(add Streamlit URL here after deployment)*

Users can paste any SMS message and instantly check whether it is spam.

---
```
## 📁 Project Structure

sms_spam_detection/
├── data/
│   └── raw/
│       └── SMSSpamCollection          # Original dataset
│
├── notebooks/
│   └── sms_spam_detection.ipynb       # EDA, preprocessing, modeling & evaluation
│
├── models/
│   └── sms_spam_lr_pipeline.pkl       # Trained TF-IDF + Logistic Regression pipeline
│
├── app/
│   └── app.py                         # Streamlit application for deployment
│
├── requirements.txt                   # Project dependencies
├── README.md                          # Project documentation
└── .gitignore                         # Ignored files and folders

```
---

## 🧰 Tools & Libraries
- Python
- Pandas, NumPy
- scikit-learn
- Streamlit
- Matplotlib, Seaborn
- Git & GitHub

---

## 🎓 Project Type
**Deployable Machine Learning Mini Project**

This project demonstrates practical ML deployment with realistic behavior and responsible evaluation.
