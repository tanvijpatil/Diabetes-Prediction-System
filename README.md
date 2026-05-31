# Diabetes Prediction System using Machine Learning, FastAPI, MLflow, BentoML, and Jenkins

## 📌 Project Overview

The Diabetes Prediction System is a Machine Learning-based application that predicts whether a patient is diabetic or not based on medical parameters such as glucose level, blood pressure, BMI, insulin level, age, and other health indicators.

This project demonstrates the complete Machine Learning lifecycle including:

* Data preprocessing
* AutoML using PyCaret
* Model training and selection
* Experiment tracking using MLflow
* API development using FastAPI
* Model deployment using BentoML
* Build automation using Jenkins
* Version control using GitHub

---

## 🎯 Objectives

* Predict diabetes using machine learning techniques.
* Automate model selection using AutoML.
* Track experiments and model versions using MLflow.
* Expose prediction services through REST APIs.
* Deploy the model using BentoML.
* Automate training workflows using Jenkins.

---

## 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Pandas       | Data Processing      |
| PyCaret      | AutoML               |
| Scikit-Learn | Machine Learning     |
| FastAPI      | REST API Development |
| Swagger UI   | API Documentation    |
| MLflow       | Experiment Tracking  |
| BentoML      | Model Deployment     |
| Jenkins      | Automation           |
| GitHub       | Version Control      |

---

## 📂 Project Structure

```text
Diabetes_Prediction_System/
│
├── diabetes.csv
├── diabetes_model.pkl
├── train_model.py
├── main.py
├── service.py
├── requirements.txt
├── mlflow.db
├── logs.log
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The project uses the Pima Indians Diabetes Dataset.

### Features

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age

### Target

* Outcome

  * 0 = Not Diabetic
  * 1 = Diabetic

---

## 🤖 AutoML Implementation

PyCaret AutoML is used to automatically compare multiple classification algorithms and select the best-performing model.

```python
best_model = compare_models()
```

The selected model is saved as:

```text
diabetes_model.pkl
```

---

## 🚀 FastAPI Implementation

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

### Prediction Endpoint

```http
POST /predict
```

### Sample Request

```json
{
  "Pregnancies": 8,
  "Glucose": 180,
  "BloodPressure": 90,
  "SkinThickness": 35,
  "Insulin": 250,
  "BMI": 38.5,
  "DiabetesPedigreeFunction": 1.2,
  "Age": 55
}
```

---

## 📈 MLflow Experiment Tracking

Train the model:

```bash
python train_model.py
```

Start MLflow UI:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

MLflow tracks:

* Experiments
* Training runs
* Parameters
* Model artifacts

---

## 📦 BentoML Deployment

Start BentoML service:

```bash
bentoml serve service:DiabetesService --reload
```

Open:

```text
http://127.0.0.1:3000
```

Available endpoint:

```http
POST /predict
```

---

## ⚙️ Jenkins Automation

A Jenkins Freestyle Project was created to automate model training.

### Build Command

```bat
cd /d D:\Tanvi\A52-AWDL\POE\Diabetes_Prediction_System

call venv\Scripts\activate

python train_model.py
```

Jenkins successfully executes the training workflow and provides build logs.

---

## 🔄 Project Workflow

```text
Dataset
   │
   ▼
PyCaret AutoML
   │
   ▼
Best Model Selection
   │
   ▼
Model Saved (.pkl)
   │
   ├── MLflow Tracking
   │
   ├── FastAPI API
   │
   ├── BentoML Deployment
   │
   ▼
Jenkins Automation
   │
   ▼
Prediction Result
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to project folder:

```bash
cd Diabetes_Prediction_System
```

Create virtual environment:

```bash
py -3.11 -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ✅ Results

* Successfully trained a diabetes prediction model.
* Implemented AutoML using PyCaret.
* Tracked experiments using MLflow.
* Created REST APIs using FastAPI.
* Deployed the model using BentoML.
* Automated training using Jenkins.
* Managed project using GitHub.
