import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model + columns
rfc = joblib.load("rfc.pkl")
columns = joblib.load("columns.pkl")

st.title("🌲 Forest Cover Type Prediction")

st.markdown("Fill values below (simple UI)")

# ---------------- CONTINUOUS FEATURES ----------------
elevation = st.slider("Elevation", 0, 4000, 2500)
aspect = st.slider("Aspect", 0, 360, 180)
slope = st.slider("Slope", 0, 60, 10)

hydro_h = st.slider("Horizontal Distance to Hydrology", 0, 1000, 200)
hydro_v = st.slider("Vertical Distance to Hydrology", -500, 500, 0)
road = st.slider("Horizontal Distance to Roadways", 0, 7000, 2000)

hill_9 = st.slider("Hillshade 9am", 0, 255, 200)
hill_noon = st.slider("Hillshade Noon", 0, 255, 200)
hill_3 = st.slider("Hillshade 3pm", 0, 255, 150)

fire = st.slider("Distance to Fire Points", 0, 8000, 3000)

# ---------------- WILDERNESS ----------------
st.subheader("Wilderness Area (choose one)")

w1 = st.radio("Wilderness Area", [1, 0, 0, 0], horizontal=True)

wilderness = [
    w1,  # simplify for demo (you can expand later)
    0,
    0,
    0
]

# ---------------- SOIL TYPE ----------------
st.subheader("Soil Type (choose one)")

soil = [0]*40
soil_index = st.selectbox("Select Soil Type (1–40)", list(range(1, 41)))
soil[soil_index - 1] = 1

# ---------------- FINAL INPUT ----------------
features = np.array([[
    0,  # Id ignored
    elevation,
    aspect,
    slope,
    hydro_h,
    hydro_v,
    road,
    hill_9,
    hill_noon,
    hill_3,
    fire,
    *wilderness,
    *soil
]])

# ---------------- PREDICTION ----------------
if st.button("Predict"):
    prediction = rfc.predict(features)[0]

    labels = {
        1: "Spruce/Fir",
        2: "Lodgepole Pine",
        3: "Ponderosa Pine",
        4: "Cottonwood/Willow",
        5: "Aspen",
        6: "Douglas-fir",
        7: "Krummholz"
    }

    st.success(f"🌿 Prediction: {labels[prediction]}")