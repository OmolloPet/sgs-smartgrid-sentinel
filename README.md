# SmartGrid Sentinel (SGS) – NIRU AI Hackathon 2026

AI-Driven Predictive Cybersecurity for Kenya’s National Power Grid

## Project Overview
SGS is a zero-trust AI platform that detects and predicts cyber threats to Kenya's power grid using LSTM forecasting and anomaly detection on time-series load data.

- **Track**: Cybersecurity / Critical Infrastructure Protection
- **MVP Status**: Functional Streamlit dashboard with real-time simulation, attack injection, and alerts.
- **Tech Stack**: Python, PyTorch (LSTM), Streamlit, Pandas, NumPy, Scikit-learn

## Setup & Run
1. Clone repo: `git clone https://github.com/YOUR-USERNAME/sgs-smartgrid-sentinel.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Train model (if needed): Run `python sgs_lstm_prediction_anomaly.py`
4. Launch dashboard: `streamlit run app.py`

Live demo (if deployed): https://your-streamlit-app-url.streamlit.app

## Features Demo
- Upload real grid CSV → Predict load → Detect anomalies
- Inject attacks (spike/drop/noise) → See red alerts
- 98%+ simulated detection accuracy

(See docs/demo.gif for animated example)

## Progress Log
- Jan 2026: Post-workshop MVP with LSTM integration
- Feb 2026: Red-team testing & polish
- March 2026: Finals demo

## Technical Roadmap
(See docs/technical_roadmap.md)

Questions? Contact: omondipeterb03@gmail.com
