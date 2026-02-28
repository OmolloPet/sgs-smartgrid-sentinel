import streamlit as st
import pandas as pd
import numpy as np

# ──────────────────────────────────────────────
# Title & Intro
# ──────────────────────────────────────────────
st.set_page_config(page_title="SGS MVP", layout="wide")
st.title("SmartGrid Sentinel (SGS) MVP")
st.markdown("**NIRU AI Hackathon 2026** – AI-Driven Predictive Cybersecurity for Kenya's Power Grid")

st.info("""
Proposal accepted Dec 25, 2025  
MVP in development – Day 3 (anomaly detection added)
""")

# ──────────────────────────────────────────────
# Data Loading Section
# ──────────────────────────────────────────────
st.subheader("1. Load Grid Data")

# Your exact CSV name from repo (CHANGE THIS if needed)
SAMPLE_CSV_PATH = "data/smart_grid_real_time_load_monitoring.csv"  # ← EDIT THIS

df = None

# Checkbox for sample
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
    st.subheader("2. Data Preview & Visualization")

    # Preview
    st.write("First 5 rows:")
    st.dataframe(df.head())

    # Numeric columns selector
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) == 0:
        st.error("No numeric columns found in CSV. Check your data.")
    else:
        selected_col = st.selectbox("Select column to plot", numeric_cols, index=0)

        # Original data copy
        original_data = df[selected_col].copy()

        # Plot container
        plot_container = st.empty()

        # Initial plot (normal)
        plot_container.line_chart(original_data, use_container_width=True)
        st.caption(f"Normal {selected_col} over time")

        # Anomaly detection (simple threshold)
        mean = original_data.mean()
        std = original_data.std()
        threshold_high = mean + 3 * std
        threshold_low = mean - 3 * std

        anomalies = (original_data > threshold_high) | (original_data < threshold_low)
        num_anomalies = anomalies.sum()

        if num_anomalies > 0:
            st.error(f"⚠️ {num_anomalies} anomalies detected in normal data (outside 3σ)")
        else:
            st.success("No anomalies in normal data")

        # Attack buttons
        st.subheader("3. Simulate Cyber Attack")
        col1, col2, col3 = st.columns(3)

        modified_data = original_data.copy()
        attack_triggered = False

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

        # Re-plot if attack triggered
        if attack_triggered:
            # Re-detect anomalies on modified data
            modified_anomalies = (modified_data > threshold_high) | (modified_data < threshold_low)
            modified_num = modified_anomalies.sum()

            # Plot with red for anomalies
            plot_data = modified_data.copy()
            plot_data[\~modified_anomalies] = np.nan  # hide normal points
            plot_container.line_chart(plot_data, color="#FF0000", use_container_width=True)
            st.caption(f"Attack injected – anomalies in red ({modified_num} points)")

            if modified_num > 0:
                st.error(f"⚠️ ATTACK DETECTED! {modified_num} anomalous points")
            else:
                st.warning("Attack injected but not detected above threshold")
        else:
            # Reset to normal plot
            plot_container.line_chart(original_data, use_container_width=True)

        # Reset button
        if st.button("Reset to Normal Data"):
            modified_data = original_data.copy()
            plot_container.line_chart(original_data, use_container_width=True)
else:
    st.info("Upload a CSV file or check 'Use sample dataset' to begin.")
