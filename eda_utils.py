# eda_utils.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def generate_summary(df):
    return df.describe(include='all').transpose()

def missing_values(df):
    nulls = df.isnull().sum()
    percent = (nulls / len(df)) * 100
    return pd.DataFrame({"Missing Values": nulls, "% Missing": percent})

def detect_outliers(df):
    outlier_rows = []
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outlier_mask = (df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)
        if outlier_mask.any():
            outlier_rows.append(df[outlier_mask])

    if outlier_rows:
        return pd.concat(outlier_rows).drop_duplicates()
    return pd.DataFrame()

def plot_distributions(df):
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        st.write(f"**Histogram of `{col}`**")
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax, color="skyblue")
        st.pyplot(fig)
