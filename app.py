import streamlit as st
import pandas as pd

st.title("SmartGrid Sentinel (SGS) MVP – Feb 24 Update")
st.write("Prototype dashboard for AI-driven grid cybersecurity")

st.info("Acceptance confirmed Dec 25, 2025 – MVP development in progress")

uploaded_file = st.file_uploader("Upload grid data CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV loaded successfully!")
    st.write("First 5 rows:", df.head())

    # Simple plot – assumes second column is numeric (e.g., load)
    if len(df.columns) > 1:
        st.line_chart(df.iloc[:, 1])
        st.caption("Basic plot of second column (e.g., load/power)")
    else:
        st.warning("CSV has only one column – add more data for plotting.")
else:
    st.info("Upload a CSV file to see data and basic visualization."

# Try to load sample CSV from repo if no upload
try:
    df_sample = pd.read_csv("data/smart_grid_load.csv")  # change to your exact CSV name
    st.write("Sample dataset loaded from repo:")
    st.write(df_sample.head())
    if len(df_sample.columns) > 1:
        st.line_chart(df_sample.iloc[:, 1])
except:
    st.info("Sample CSV not found yet – upload your own")
