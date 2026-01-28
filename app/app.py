import streamlit as st
import requests
import pandas as pd

# ---------------------------
# Config
# ---------------------------
API_URL = "http://api:8000/predict"

st.set_page_config(
    page_title="CO2 Emission Calculator",
    page_icon="🚗"
)

st.title("🚗 CO₂ Emission Calculator")
st.write("Predict vehicle CO₂ emissions using ML API")

# ---------------------------
# User Inputs
# ---------------------------
engine_size = st.number_input("Engine Size (L)", 0.5, 8.0, 2.0)
cylinders = st.selectbox("Cylinders", [3, 4, 5, 6, 8, 10, 12])
fuel_type = st.selectbox("Fuel Type", ["X", "Z", "D", "E", "N"])
fuel_city = st.number_input("Fuel Consumption City (L/100km)", 2.0, 30.0, 9.0)
fuel_hwy = st.number_input("Fuel Consumption Highway (L/100km)", 2.0, 25.0, 7.0)
vehicle_class = st.selectbox(
    "Vehicle Class",
    [
        "COMPACT",
        "MID-SIZE",
        "FULL-SIZE",
        "SUV - SMALL",
        "SUV - STANDARD",
        "PICKUP TRUCK - STANDARD",
        "MINIVAN",
        "SUBCOMPACT"
    ]
)

# ---------------------------
# Predict
# ---------------------------
if st.button("🔍 Predict CO₂"):

    payload = {
        "engine_size": engine_size,
        "cylinders": cylinders,
        "fuel_type": fuel_type,
        "fuel_city": fuel_city,
        "fuel_hwy": fuel_hwy,
        "vehicle_class": vehicle_class
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()["co2_emission_g_km"]

        st.success(f"🌱 Estimated CO₂ Emission: **{result} g/km**")

        if result < 150:
            st.info("✅ Low emission vehicle")
        elif result < 200:
            st.warning("⚠️ Moderate emission vehicle")
        else:
            st.error("🚨 High emission vehicle")
    else:
        st.error("API Error. Check backend.")
