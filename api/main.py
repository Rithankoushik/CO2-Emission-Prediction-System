from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("co2_emission_model.pkl")

app = FastAPI(
    title="CO2 Emission Prediction API",
    description="Predict CO2 emissions based on vehicle specs",
    version="1.0"
)

# ---------------------------
# Input Schema
# ---------------------------
class CarInput(BaseModel):
    engine_size: float
    cylinders: int
    fuel_type: str
    fuel_city: float
    fuel_hwy: float
    vehicle_class: str

# ---------------------------
# Prediction Endpoint
# ---------------------------
@app.post("/predict")
def predict_co2(data: CarInput):

    input_df = pd.DataFrame({
        "Engine Size(L)": [data.engine_size],
        "Cylinders": [data.cylinders],
        "Fuel Type": [data.fuel_type],
        "Fuel Consumption City (L/100 km)": [data.fuel_city],
        "Fuel Consumption Hwy (L/100 km)": [data.fuel_hwy],
        "Vehicle Class": [data.vehicle_class]
    })

    prediction = model.predict(input_df)[0]

    return {
        "co2_emission_g_km": round(float(prediction), 2)
    }
