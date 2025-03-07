import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

# Load trained model
model_file = 'XGB.pkl'

try:
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model not found! Please upload the model before making predictions.")
    st.stop()

# App title
st.title("Vinhos Raposinha, The ML App")
st.subheader("Wine Quality Prediction")

# Background styling
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://th.bing.com/th/id/OIP.1LE1WdwJ03addVqzrrDLGAHaEK?rs=1&pid=ImgDetMain");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# User inputs for model features
st.subheader("Enter Wine Features")

fixed_acidity = st.number_input("Fixed Acidity", value=7.0, step=0.1)
volatile_acidity = st.number_input("Volatile Acidity", value=0.3, step=0.01)
citric_acid = st.number_input("Citric Acid", value=0.3, step=0.01)
residual_sugar = st.number_input("Residual Sugar", value=2.0, step=0.1)
chlorides = st.number_input("Chlorides", value=0.05, step=0.001)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=15.0, step=1.0)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=45.0, step=1.0)
density = st.number_input("Density", value=0.99, step=0.001)
ph = st.number_input("pH", value=3.2, step=0.01)
sulphates = st.number_input("Sulphates", value=0.5, step=0.01)
alcohol = st.number_input("Alcohol", value=10.0, step=0.1)
wine_type = st.selectbox("Wine Type", ["White", "Red"])
# Convert wine type to numeric (0 = Red, 1 = White) 
wine_type_encoded = 1 if wine_type == "White" else 0


# Preprocessing function before prediction
def preprocess_input(data):
    # Load scaler and imputer from training (or train based on input data)
    scaler = MinMaxScaler()
    

    # Create temporary DataFrame to apply transformations
    df_temp = pd.DataFrame(data, index=[0])


    # Apply MinMaxScaler
    df_temp_scaled = scaler.fit_transform(df_temp)

    return df_temp_scaled

# Prediction button
if st.button("Predict Quality"):
    input_features = {
        "fixed acidity": fixed_acidity,
        "volatile acidity": volatile_acidity,
        "citric acid": citric_acid,
        "residual sugar": residual_sugar,
        "chlorides": chlorides,
        "free sulfur dioxide": free_sulfur_dioxide,
        "total sulfur dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": ph,
        "sulphates": sulphates,
        "alcohol": alcohol,
        "type": wine_type_encoded,
    }

    # Preprocess input before prediction
    processed_input = preprocess_input(input_features)
    # Make prediction
    prediction = model.predict(processed_input)

    # Display result with interpretation
    if prediction[0] == 0:
        st.error("The predicted wine quality is **LOW** ❌")
    else:
        st.success("The predicted wine quality is **HIGH** ✅")