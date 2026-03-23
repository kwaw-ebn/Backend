from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1️⃣ Create FastAPI instance
app = FastAPI(title="Malaria Prediction API")

# 2️⃣ Load trained model
model = joblib.load("malaria_model.pkl")

# Optional: load features
try:
    features = joblib.load("features.pkl")
except:
    features = [
        'rainfall_lag1', 'rainfall_lag2', 'rainfall_lag3',
        'temp_lag1', 'humidity_lag1',
        'rainfall_avg_3', 'temp_avg_3',
        'month_num', 'quarter'
    ]

# 3️⃣ Pydantic model for input validation
class PredictionInput(BaseModel):
    rainfall_lag1: float
    rainfall_lag2: float
    rainfall_lag3: float
    temp_lag1: float
    humidity_lag1: float
    rainfall_avg_3: float
    temp_avg_3: float
    month_num: int
    quarter: int

# 4️⃣ Root endpoint
@app.get("/")
def home():
    return {"message": "API is running 🚀"}

# 5️⃣ Prediction endpoint
@app.post("/predict")
def predict(data: PredictionInput):
    # Convert Pydantic model to DataFrame
    df = pd.DataFrame([data.dict()])
    
    # Ensure correct feature order
    df = df[features]

    # Make prediction
    prediction = model.predict(df)[0]

    # Risk classification
    if prediction > 500:
        risk = "High 🔴"
    elif prediction > 200:
        risk = "Medium 🟡"
    else:
        risk = "Low 🟢"

    return {
        "prediction": int(prediction),
        "risk": risk
    }
