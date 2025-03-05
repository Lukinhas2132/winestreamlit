import streamlit as st
import pandas as pd
st.title("Vinhosinho")
st.subheader("Table")

df_wine = pd.read_csv(r"C:\Users\graci\OneDrive\Desktop\winestreamlit\W_R_quality.csv")
st.dataframe(df_wine)


