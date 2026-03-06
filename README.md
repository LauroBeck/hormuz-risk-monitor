# 📉 2026 Hormuz Crisis: Semicap Risk Monitor
![Status](https://img.shields.io/badge/Market_Status-Mar_05_Rebound-green)
![Python](https://img.shields.io/badge/Python-3.12+-blue)

## 📌 Project Overview
This repository provides real-time risk analytics for the South Korean semiconductor sector during the **2026 Strait of Hormuz blockade**. It is calibrated for the extreme volatility regime triggered by regional conflict and state-led liquidity injections.

## 📊 Mar 05, 2026 Session Summary
* **Asset:** SK Hynix (000660.KS)
* **Closing Price:** 941,000 KRW (+10.84%)
* **Market Event:** Buy-side Sidecar triggered at 09:06 AM KST.
* **Portfolio VaR (95%):** **$244,314.60** per $1M exposure.

## 🛠️ Components
* `run_pipeline.py`: Automated EOD analysis (scheduled for 15:45 KST).
* `src/`: Defensive processing logic for KRX Sidecar rules.
* `docs/`: Protocol for the **$68B Market Stability Fund (MSF)**.
* `tests/`: Automated integrity checks for volatility triggers.

## 🚀 Usage
```bash
pip install -r requirements.txt
python3 run_pipeline.py
```
