import streamlit as st
import pandas as pd
import numpy as np

st.title("SmartGrid Sentinel MVP – Day 2")
st.write("AI-Driven Predictive Cybersecurity for Kenya's Power Grid")

st.info("Proposal accepted Dec 25, 2025 – MVP in development")

# Path to your sample CSV (change to your exact file name)
SAMPLE_CSV_PATH = "data/smart_grid_real_time_load_monitoring.csv"  # EDIT THIS

df = None

# Load sample from repo if checked
use_sample = st.checkbox("Use sample dataset from repo", value=True)

if use_sample:
    try:
        df = pd.read_csv(SAMPLE_CSV_PATH)
        st.success(f"Sample CSV loaded: {SAMPLE_CSV_PATH}")
    except FileNotFoundError:
        st.warning("Sample CSV not found – upload your own")

# Allow user upload (overrides sample)
uploaded_file = st.file_uploader("Upload your own grid CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Uploaded CSV loaded!")

# If data is loaded, show preview and plot
if df is not None:
    st.write("Preview (first 5 rows):")
    st.dataframe(df.head())

    # Find numeric columns
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) == 0:
        st.error("No numeric columns found in CSV – check data")
    else:
        selected_col = st.selectbox("Select column to plot", numeric_cols, index=0)
        original_data = df[selected_col].copy()  # Keep original for reset

        # Plot area
        plot_container = st.empty()

        # Attack buttons
        col1, col2, col3 = st.columns(3)
        if col1.button("Inject Spike"):
            modified = original_data.copy()
            spike_start = np.random.randint(0, len(modified)-50)
            modified[spike_start:spike_start+50] += np.random.uniform(10, 30, 50)  # random spike
            plot_container.line_chart(modified)
            st.warning("Spike attack injected!")
        elif col2.button("Inject Drop"):
            modified = original_data.copy()
            drop_start = np.random.randint(0, len(modified)-50)
            modified[drop_start:drop_start+50] -= np.random.uniform(10, 30, 50)  # random drop
            plot_container.line_chart(modified)
            st.warning("Drop attack injected!")
        elif col3.button("Inject Noise"):
            modified = original_data.copy()
            noise = np.random.normal(0, 5, len(modified))  # random noise
            modified += noise
            plot_container.line_chart(modified)
            st.warning("Noise attack injected!")
        else:
            # Default: show original
            plot_container.line_chart(original_data)
            st.caption(f"Normal {selected_col} over time")

        # Reset button
        if st.button("Reset Plot"):
            plot_container.line_chart(original_data)
else:
    st.info("Upload CSV or check 'Use sample dataset' to begin")
