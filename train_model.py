import pandas as pd
from pycaret.classification import *

# Load dataset
data = pd.read_csv("diabetes.csv")

# Setup PyCaret
clf = setup(
    data=data,
    target='Outcome',
    session_id=123
)

# Compare models
best_model = compare_models()

# Save model
save_model(best_model, 'diabetes_model')

print("Model trained successfully!")