import joblib
import numpy as np
import streamlit as st

# Load the saved model 
model = joblib.load('./02_clean_data/stroke_model.pkl')

st.title("🧠 Stroke Prediction App")
st.write("Enter the details below to predict the likelihood of a stroke")

# User input
Gender = st.selectbox("Gender",["Male","Female","Other"])
Age = st.slider("Age", 0, 100, 25)
Hypertension = st.selectbox("Hypertension", ["No", "Yes"])
Heart_Disease = st.selectbox("Heart Disease", ["No", "Yes"])
Ever_Married = st.selectbox("Ever Married", ["No", "Yes"])
Work_Type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"])
Residence_Type = st.selectbox("Residence Type", ["Urban", "Rural"])
Avg_glucose_level = st.number_input("Average Glucose Level")
Bmi = st.number_input("BMI")
Smoking_status = st.selectbox("Smoking Status", ["never smoked", "formerly smoked", "smokes", "Unknown"])

# Map inputs to numerical values
gender_map = {"Male": 1, "Female": 0, "Other": 2}
hypertension_map = {"No": 0, "Yes": 1}
heart_disease_map = {"No": 0, "Yes": 1}
married_map = {"No": 0, "Yes": 1}
work_type_map = {"Private": 0, "Self-employed": 1, "Children": 2, "Govt_job": 3, "Never_worked": 4}
residence_map = {"Urban": 1, "Rural": 0}
smoking_map = {"never smoked": 1, "formerly smoked": 0, "smokes": 2, "Unknown": 3}

# Create input array
input_data = np.array([[
    gender_map[Gender],
    Age,
    hypertension_map[Hypertension],
    heart_disease_map[Heart_Disease],
    married_map[Ever_Married],
    work_type_map[Work_Type],
    residence_map[Residence_Type],
    Avg_glucose_level,
    Bmi,
    smoking_map[Smoking_status]
]])

# st.write("Model type:", type(model))

# Predict 
if st.button("Predict Stroke"): 
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]  # Probability of class '1'
    if prediction == 1:
        st.error(f"High risk of stroke ({probability:.2%} confidence)")
    else: 
        st.success(f"Low risk of stroke({probability:.2%} confidence)")
