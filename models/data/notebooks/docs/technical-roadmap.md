# Technical Roadmap – SmartGrid Sentinel (SGS)  
NIRU AI Hackathon 2026  
Peter Omondi  
February 24, 2026

## 1. Project Summary

**Objective**  
Build a Minimum Viable Product (MVP) that demonstrates real-time anomaly detection and predictive threat forecasting on power grid time-series data to identify and mitigate cyber-physical attacks (false data injection, suppression, noise flooding).

**Core MVP Features**  
- Interactive Streamlit dashboard for data upload, visualization, and simulation  
- LSTM model for forecasting normal grid load behavior  
- Anomaly detection based on prediction errors  
- Simulated attack injection (spike / drop / noise) with visual alerts  
- Basic auto-remediation mock (alert + simulated node isolation)

**Technology Stack**  
- Python 3  
- Streamlit (dashboard)  
- PyTorch (LSTM forecasting)  
- Pandas / NumPy (data processing)  
- Matplotlib (plots)  
- Public datasets (Kaggle Smart Grid, IEEE DataPort)

## 2. Current Status (February 24, 2026)

- Proposal accepted December 25, 2025  
- Pre-hackathon workshop (January 19–20) completed  
- GitHub repo created and linked to NIRU portal  
- Health Score: 28 (Stable)  
- Milestone 1 active ("GitHub Setup & Initial MVP Skeleton")  
- Basic app.py added (CSV upload + simple plot)  
- Technical Roadmap submitted to portal yesterday (Feb 23)  
- No fully integrated MVP running yet  
- No real dataset integrated (synthetic data only)

## 3. Milestones & Timeline (February 24 – March 2026)

| Phase                          | Dates                  | Key Tasks & Deliverables                                                                 | Success Metric / Output                              |
|--------------------------------|------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------|
| Phase 1: Foundation & Compliance | Feb 24 – Feb 28 (5 days) | - Update repo with today's progress<br>- Add CSV loader to app.py<br>- Finalize milestone 1 deliverables<br>- Commit daily | - Repo has ≥8 commits<br>- Milestone 1 complete<br>- CSV upload working |
| Phase 2: Core MVP Build        | Mar 1 – Mar 10 (10 days) | - Integrate public dataset (Kaggle Smart Grid CSV)<br>- Train lightweight LSTM on normal data (Colab)<br>- Implement anomaly detection<br>- Add attack simulator<br>- Build full dashboard: predict → detect → alerts | - Dashboard runs locally<br>- Detects anomalies in 3+ tests<br>- Repo updated with core files |
| Phase 3: Testing & Polish      | Mar 11 – Mar 18 (8 days) | - Run red-team tests<br>- Add explainable alerts<br>- Record 1–2 min demo GIF/video<br>- Deploy to Streamlit Cloud<br>- Update README with demo link | - Demo GIF in repo<br>- Live URL working<br>- ≥95% detection in tests |
| Phase 4: Finals Preparation    | Mar 19 – Finals        | - Rehearse 3–5 min pitch<br>- Prepare 5–8 slides<br>- Final bug fixes<br>- Backup everything | - Presentation rehearsed<br>- Stable MVP demo<br>- Ready for showcase |

## 4. Risks & Mitigation

- **Risk**: No real KPLC data → **Mitigation**: Use public Kaggle/IEEE datasets; note real integration follows pilot  
- **Risk**: Limited compute → **Mitigation**: Use free Google Colab GPU; keep model small  
- **Risk**: Time constraints (solo) → **Mitigation**: Prioritize core loop (data → forecast → detect → alert)  
- **Risk**: Portal/repo tracking → **Mitigation**: Daily commits + screenshot submissions

## 5. Support Requests

- Feedback from mentor Ambrose on roadmap priorities  
- Any NIRU-provided GPU/cloud credits  
- Clarification on exact finals date/format

## GitHub Repository
https://github.com/OmolloPet/sgs-smartgrid-sentinel

**Commitment**: Daily/regular commits (code, README, docs). Progress tracked via portal.
