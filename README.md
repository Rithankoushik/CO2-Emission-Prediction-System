🚗 CO₂ Emission Prediction System (ML + API + UI)
📌 Overview

This project implements an end-to-end machine learning system to predict vehicle CO₂ emissions (g/km) based on engine specifications and fuel consumption data.
The solution is built using a production-style architecture with a trained ML model exposed via a FastAPI backend and consumed by a Streamlit frontend.

The system is designed for automotive manufacturers to support:

Emission analysis

Sustainability initiatives

Regulatory compliance

Design and benchmarking decisions

🏗️ System Architecture
User (Streamlit UI)
        ↓
   REST API (FastAPI)
        ↓
   ML Model (Scikit-learn Pipeline)

📂 Project Structure

Co2-prediction/
│
├── api/
│   ├── main.py                  # FastAPI backend
│   ├── co2_emission_model.pkl   # Trained ML model
│
├── app/
│   └── app.py                   # Streamlit UI
│
├── requirements.txt             # Dependency versions
└── README.md

📊 Dataset

Vehicle CO₂ Emissions Dataset (Canada)
Source: Kaggle (Government of Canada open data)

Target Variable

CO2 Emissions(g/km)

Key Features Used

Engine Size (L)

Cylinders

Fuel Type

Fuel Consumption City (L/100 km)

Fuel Consumption Highway (L/100 km)

Vehicle Class

This dataset represents real-world regulatory vehicle emission data, making it suitable for industrial use cases.

🧠 Machine Learning Approach

Problem Type: Supervised Learning (Regression)

Models Used:

Linear Regression (baseline)

Random Forest Regressor (final model)

Preprocessing:

StandardScaler for numeric features

OneHotEncoder for categorical features

ColumnTransformer + Pipeline

Evaluation Metrics:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score

🚀 Features

REST API for model inference

Interactive Streamlit UI for user input

Real-time CO₂ emission prediction

Clean separation between model, API, and UI

Scalable and reusable architecture

⚙️ Setup Instructions
1️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt


⚠️ Important:
The scikit-learn version must match the version used during model training to avoid pickle errors.

▶️ Running the API (FastAPI)
cd api
uvicorn main:app --reload


API URL: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

▶️ Running the Streamlit App

Open a new terminal:

cd app
streamlit run app.py


The UI allows users to:

Enter vehicle specifications

Call the backend API

View predicted CO₂ emissions instantly

🔌 API Endpoint
POST /predict

Request Body

{
  "engine_size": 2.0,
  "cylinders": 4,
  "fuel_type": "X",
  "fuel_city": 9.5,
  "fuel_hwy": 7.2,
  "vehicle_class": "COMPACT"
}


Response

{
  "co2_emission_g_km": 196.45
}

📈 Business Impact

Identifies key emission drivers (engine size, fuel consumption)

Enables rapid emission estimation during vehicle design

Supports sustainability and compliance analysis

Can be integrated into internal automotive analytics tools

