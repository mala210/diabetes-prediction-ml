import streamlit as st
import numpy as np
import joblib

# App title
st.title("Diabetes Prediction App")

st.write("Enter patient information below:")

# User inputs
age = st.number_input("Age", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)

# Load trained model
try:
    model = joblib.load("model.pkl")
except:
    st.warning("Model file not found. Please upload model.pkl to your repository.")
    model = None

# Prediction button
if st.button("Predict"):
    if model is not None:
        # Prepare input data
        input_data = np.array([[age, glucose, bmi]])

        # Make prediction
        prediction = model.predict(input_data)

        # Show result
        if prediction[0] == 1:
            st.error("Prediction: Diabetic")
        else:
            st.success("Prediction: Not Diabetic")
    else:
        st.info("Model is not available yet.")
