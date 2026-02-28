# SmartGrid Sentinel (SGS) – NIRU AI Hackathon 2026

AI-Driven Predictive Cybersecurity for Kenya's National Power Grid

## Project Overview
SGS is a zero-trust AI platform designed to detect and predict cyber threats to Kenya's power grid.  
It uses LSTM-based forecasting and anomaly detection on time-series load data to identify attacks (e.g., false data injection, suppression, noise flooding).

**Track**: Cybersecurity / Critical Infrastructure Protection

**MVP Goal**: Interactive Streamlit dashboard that:
- Loads grid data (CSV)
- Forecasts normal behavior
- Detects anomalies with visual alerts
- Simulates attacks for testing

## Current Status – February 24, 2026
- Proposal accepted: December 25, 2025
- Pre-hackathon workshop (Jan 19–20) completed
- Repo linked to NIRU portal
- Health Score: 28 (Stable)
- Milestone 1 active ("GitHub Setup & Initial MVP Skeleton")
- Basic app.py added (CSV upload + simple plot)

## Tech Stack
- Python
- Streamlit (dashboard)
- PyTorch (LSTM forecasting)
- Pandas / NumPy (data handling)
- Matplotlib (visualization)
- Public datasets (Kaggle Smart Grid, IEEE DataPort)

## Setup (when running locally)
1. `git clone https://github.com/OmolloPet/sgs-smartgrid-sentinel.git`
2. `pip install -r requirements.txt`
3. `streamlit run app.py`

## Next Steps
- Integrate real dataset
- Add LSTM forecasting + anomaly detection
- Record demo GIF
- Deploy to Streamlit Cloud

## Technical Roadmap
See [docs/technical-roadmap.md](docs/technical-roadmap.md)

Contact: peteromondi03@gmail.com

## Progress – February 25, 2026
- Fixed technical-roadmap.md path (no more 404)
- Milestone 1 deliverables almost complete
- Preparing to add dataset loader next

## Progress – February 27, 2026
- Added sample grid CSV to data/ folder
- Updated app.py to load real data
- Preparing attack injection and anomaly detection next
- Mentor meeting feedback incorporated

## Progress – February 28, 2026
- Uploaded sample smart grid CSV to data/ folder
- Updated app.py to auto-load repo CSV or uploaded file
- Added attack injection buttons to app.py (spike, drop, noise)
- Dashboard now simulates cyber attacks
- Next: anomaly detection alerts
