# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from eda_utils import generate_summary, plot_distributions, missing_values, detect_outliers

st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("📊 Auto EDA Dashboard")
st.markdown("Upload your dataset (CSV) to explore insights instantly.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📈 Summary Statistics")
    st.dataframe(generate_summary(df))

    st.subheader("🕳️ Missing Values")
    st.dataframe(missing_values(df))

    st.subheader("🚨 Outlier Detection")
    outliers_df = detect_outliers(df)
    if outliers_df.empty:
        st.info("No major outliers detected.")
    else:
        st.dataframe(outliers_df)

    st.subheader("📊 Distribution Plots")
    plot_distributions(df)
