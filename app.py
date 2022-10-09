import pandas as pd
import streamlit as st
from joblib import load
st.title("Bird-classification-app")
st.subheader("Welcome you")

uploaded_file=st.file_uploader("choose a excel file with PCA")
if uploaded_file is not None:
    df1=pd.read_csv(uploaded_file)

else:
    st.warning("you need to upload a csv or excel file")


uploaded_file=st.file_uploader("choose a excel file with standardized data")
if uploaded_file is not None:
    df1=pd.read_csv(uploaded_file)

else:
    st.warning("you need to upload a csv or excel file")

data=st.file_uploader("choose the CSV file containg vector to be predicted upon")
model=st.file_uploader("choose classifier joblib file")


if data is not None and model is not None:
    data=pd.read_csv(data).values
    model=load(model)
    predictions=model.predict(data)
    st.write(predictions)
