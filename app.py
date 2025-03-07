import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model and preprocessor
model_file = 'random_forest_model.pkl'

# Load the model from the pickle file

with open(model_file, 'rb') as file:
    model = pickle.load(file)

st.title("Vinhosinho The ML App")
st.subheader("Wine QualityTable")

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("https://th.bing.com/th/id/OIP.1LE1WdwJ03addVqzrrDLGAHaEK?rs=1&pid=ImgDetMain");
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

with st.expander('data'):
    st.write('**Cleaned data**')
    df_wine = pd.read_csv(r"C:\Users\graci\OneDrive\Desktop\winestreamlit\W_R_quality.csv")
    st.dataframe(df_wine)


st.subheader("Predict Wine Quality")

try:
    model = load_model("random_forest_model.pkl")
    st.success("Model loaded successfully!")
except:
    model = None
    st.warning("Model not found. Please train the model first.")

    if model is not None:
    st.write("Enter wine features below to predict the quality.")

    fixed_acidity = st.number_input("Fixed Acidity", value=7.0, step=0.1)
    ph = st.number_input("pH", value=3.2, step=0.01)
    alcohol = st.number_input("Alcohol", value=10.0, step=0.1)
        if st.button("Predict Quality"):
        ## I need to Create a input features that match the model
        input_features = {
            "fixed acidity": fixed_acidity,
            "pH": ph,
            "alcohol": alcohol,
            ## ... add the rest
        }
        prediction = predict_quality(model, input_features)
        st.success(f"Predicted Wine Quality: {prediction}")

else:
    st.info("Train the model or ensure the model file is available before making a prediction.")