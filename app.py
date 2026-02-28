import streamlit as st
import pandas as pd

st.title("SmartGrid Sentinel MVP – Feb 28")
st.write("AI threat detection for Kenya's power grid")

# Try to load sample CSV from repo first
sample_path = "data/smart_grid_load.csv"  # CHANGE to your exact CSV name
df = None

try:
    df = pd.read_csv(sample_path)
    st.success("Sample dataset from repo loaded!")
except:
    st.info("Sample CSV not found – upload your own")

# Allow upload override
uploaded_file = st.file_uploader("Upload your own grid CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Uploaded CSV loaded!")

if df is not None:
    st.write("Preview (first 5 rows):", df.head())

    # Plot first numeric column (adjust index if needed)
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        st.line_chart(df[numeric_cols[0]])
        st.caption(f"Plot of {numeric_cols[0]} over time")
    else:
        st.warning("No numeric columns found – check CSV")
else:
    st.info("Upload CSV or place sample in data/ folder")
