from fastapi import FastAPI
from pydantic import BaseModel
from pycaret.classification import load_model, predict_model
import pandas as pd

# Load model
model = load_model('diabetes_model')

app = FastAPI()

# Input schema
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Home route
@app.get("/")
def home():
    return {"message": "Diabetes Prediction API"}

# Prediction route
@app.post("/predict")
def predict(data: DiabetesInput):

    input_data = pd.DataFrame([{
        "Pregnancies": data.Pregnancies,
        "Glucose": data.Glucose,
        "BloodPressure": data.BloodPressure,
        "SkinThickness": data.SkinThickness,
        "Insulin": data.Insulin,
        "BMI": data.BMI,
        "DiabetesPedigreeFunction": data.DiabetesPedigreeFunction,
        "Age": data.Age
    }])

    prediction = predict_model(model, data=input_data)

    result = int(prediction['prediction_label'][0])

    return {
        "prediction": "Diabetic" if result == 1 else "Not Diabetic"
    }