# 🌲 Forest Cover Type Prediction Using Machine Learning

A machine learning project that predicts the type of forest cover based on cartographic and environmental features using a trained Random Forest Classifier, deployed as an interactive Streamlit web app.

---

## 🚀 Live Project Features

- 🌲 Predict forest cover type (7 classes)
- 🧠 Machine Learning model (Random Forest)
- 📊 Uses real-world forestry dataset
- 🌐 Simple Streamlit web interface
- ⚡ Fast predictions
- 🎯 User-friendly input system (no complex manual encoding)

---

## 📌 Problem Statement

Forests cover a large portion of Earth's surface, and understanding forest composition is important for:

- Environmental monitoring
- Biodiversity studies
- Land management
- Conservation planning

The goal is to predict forest cover type based on geographic and soil conditions using machine learning.

---

## 🌳 Forest Cover Types (Target Classes)

| Label | Cover Type |
|------|------------|
| 1 | Spruce/Fir |
| 2 | Lodgepole Pine |
| 3 | Ponderosa Pine |
| 4 | Cottonwood/Willow |
| 5 | Aspen |
| 6 | Douglas-fir |
| 7 | Krummholz |

---

## 📊 Dataset Description

This dataset contains **55 input features** describing forest plots of size 30m x 30m.

### Key Feature Groups:

- Elevation
- Aspect
- Slope
- Hydrology distances
- Road & fire distances
- Hillshade (sunlight exposure)
- Wilderness areas
- Soil types

---

## 🧠 Input Features Explained

### 🌄 Terrain Features
- Elevation → Height above sea level  
- Aspect → Direction slope faces  
- Slope → Steepness of terrain  

---

### 💧 Hydrology Features
- Horizontal_Distance_To_Hydrology → Distance to water bodies  
- Vertical_Distance_To_Hydrology → Elevation difference to water  

---

### 🛣️ Infrastructure Features
- Horizontal_Distance_To_Roadways → Distance to roads  
- Horizontal_Distance_To_Fire_Points → Distance to fire locations  

---

### 🌞 Hillshade Features
- Hillshade_9am → Morning sunlight  
- Hillshade_Noon → Midday sunlight  
- Hillshade_3pm → Afternoon sunlight  

---

### 🌲 Wilderness Areas (One-Hot Encoded)
- Wilderness_Area1 → Rawah Wilderness Area  
- Wilderness_Area2 → Neota Wilderness Area  
- Wilderness_Area3 → Comanche Peak Wilderness Area  
- Wilderness_Area4 → Cache la Poudre Wilderness Area  

---

### 🌱 Soil Types (40 Categories)
- Soil_Type1 → Soil_Type40  
Represents soil composition such as:
- volcanic soil  
- rocky soil  
- sandy soil  
- clay soil  
- organic forest soil  

---

## 🧠 Machine Learning Model

### Model Used:
- RandomForestClassifier (Scikit-learn)

### Why Random Forest?
- Works well on tabular data  
- Handles many features  
- Reduces overfitting  
- High accuracy  

---

## 📈 Model Pipeline

1. Load dataset  
2. Preprocess features  
3. Train-test split  
4. Train Random Forest model  
5. Evaluate accuracy  
6. Save model using pickle  
7. Deploy using Streamlit  

---

## 🎯 Model Performance

- Accuracy: ~85–90%  
- Stable and robust predictions  

---

## 🖥️ Web App Workflow

1. User enters environmental values  
2. Data is converted into feature vector  
3. Model predicts forest cover type  
4. Result is displayed instantly  

---

## 📦 Tech Stack

- Python 🐍  
- Pandas & NumPy  
- Scikit-learn 🤖  
- Streamlit 🌐  
- Pickle (Model Saving)  

---