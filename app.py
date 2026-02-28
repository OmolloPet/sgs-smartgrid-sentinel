import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SGS MVP", layout="wide")
st.title("SmartGrid Sentinel (SGS) MVP")
st.markdown("**NIRU AI Hackathon 2026** – AI-Driven Predictive Cybersecurity for Kenya's Power Grid")

st.info("Proposal accepted Dec 25, 2025 – MVP in development")

# Path to your sample CSV – CHANGE THIS to your exact file name
SAMPLE_CSV_PATH = "data/smart_grid_real_time_load_monitoring.csv"  # ← CHANGE TO YOUR EXACT FILE NAME

df = None

# Load sample from repo if checked
use_sample = st.checkbox("Load sample dataset from repo (if available)", value=False)

if use_sample:
    try:
        df = pd.read_csv(SAMPLE_CSV_PATH)
        st.success(f"Sample data loaded from: {SAMPLE_CSV_PATH}")
    except FileNotFoundError:
        st.warning(f"Sample file not found at '{SAMPLE_CSV_PATH}'. Upload your own CSV below.")
    except Exception as e:
        st.error(f"Error loading sample: {e}")

# File uploader (always available)
uploaded_file = st.file_uploader("Upload your own grid CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Uploaded CSV loaded successfully!")
    except Exception as e:
        st.error(f"Error loading uploaded file: {e}")

# ──────────────────────────────────────────────
# Show Data & Plot
# ──────────────────────────────────────────────
if df is not None:
    st.subheader("Data Preview & Visualization")

    # Preview
    st.write("First 5 rows:")
    st.dataframe(df.head())

    # Numeric columns selector
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) == 0:
        st.error("No numeric columns found in CSV. Check your data.")
    else:
        selected_col = st.selectbox("Select column to plot", numeric_cols, index=0)
        original_data = df[selected_col].copy()  # Keep original

        # Plot area
        plot_container = st.empty()

        # Attack buttons
        st.subheader("Simulate Cyber Attack")
        col1, col2, col3 = st.columns(3)

        attack_triggered = False
        modified_data = original_data.copy()

        if col1.button("Inject Spike"):
            spike_start = np.random.randint(0, len(modified_data)-50)
            modified_data[spike_start:spike_start+50] += np.random.uniform(10, 30, 50)
            attack_triggered = True
            st.warning("Spike attack injected!")

        if col2.button("Inject Drop"):
            drop_start = np.random.randint(0, len(modified_data)-50)
            modified_data[drop_start:drop_start+50] -= np.random.uniform(10, 30, 50)
            attack_triggered = True
            st.warning("Drop attack injected!")

        if col3.button("Inject Noise"):
            noise = np.random.normal(0, 5, len(modified_data))
            modified_data += noise
            attack_triggered = True
            st.warning("Noise attack injected!")

        # Anomaly detection (simple threshold on original data)
        mean = original_data.mean()
        std = original_data.std()
        threshold_high = mean + 3 * std
        threshold_low = mean - 3 * std

        # Detect on current data (modified or original)
        anomalies = (modified_data > threshold_high) | (modified_data < threshold_low)
        num_anomalies = anomalies.sum()

        # Plot with red for anomalies
        plot_data = modified_data.copy()
        plot_data[\~anomalies] = np.nan  # Hide normal points (keep only anomalies)
        color = "#FF0000" if num_anomalies > 0 else "#1f77b4"
        plot_container.line_chart(plot_data, color=color, use_container_width=True)
        st.caption(f"Plot of {selected_col} – red = anomalies ({num_anomalies} points)")

        # Alert message
        if num_anomalies > 0:
            st.error(f"⚠️ ANOMALY DETECTED! {num_anomalies} points outside normal range (3σ)")
        elif attack_triggered:
            st.warning("Attack injected but no anomaly detected above threshold")
        else:
            st.success("Normal operation – no anomalies detected")

        # Reset button
        if st.button("Reset to Normal Data"):
            modified_data = original_data.copy()
            plot_container.line_chart(original_data, color="#1f77b4", use_container_width=True)
else:
    st.info("Upload a CSV file or check 'Use sample dataset' to begin.")
