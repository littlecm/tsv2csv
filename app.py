import streamlit as st
import pandas as pd
import numpy as np

def load_tsv(file):
    """Load a TSV file and return a DataFrame."""
    return pd.read_csv(file, sep='\t')

def calculate_blank_percentage(df):
    """Calculate the percentage of blank values in each column of a DataFrame."""
    blank_percentage = df.isna().mean().round(4) * 100  # Calculate NaN percentage
    return blank_percentage

# Streamlit UI
st.title('TSV to CSV Converter & Data Analyzer')

uploaded_file = st.file_uploader("Choose a TSV file", type="tsv")

if uploaded_file is not None:
    # Load and display the TSV data
    data = load_tsv(uploaded_file)
    st.write("## Original TSV Data")
    st.dataframe(data.style.highlight_null(null_color='red'))

    # Convert DataFrame to CSV and allow download
    csv = data.to_csv(index=False)
    st.download_button(label="Download data as CSV", data=csv, file_name='converted.csv', mime='text/csv')

    # Calculate and display blank value percentages
    st.write("## Percentage of Blank Values by Column")
    blank_percentage = calculate_blank_percentage(data)
    st.bar_chart(blank_percentage)
