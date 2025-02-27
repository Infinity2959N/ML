from joblib import load
import numpy as np
import streamlit as st

#Load model:
model= load('model.pkl')

st.title("Placement Package Prediction")
st.write("Enter your CGPA")

cgpa_input= st.number_input("CGPA", max_value=10.0, min_value=0.0, step=0.1)

if st.button("Predict"):
    inputf= np.array([[cgpa_input]])
    prediction= model.predict(inputf)[0]
    st.success(f"Your predicted package is: {prediction} LPA")