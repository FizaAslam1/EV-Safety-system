# 🚗 EV-Safety System: AI-Powered Predictive Maintenance for EV Chargers

Predict electric vehicle charger failures 7 days in advance with 99% accuracy, enabling proactive maintenance and preventing costly downtime.

## 🎯 Live Demo

Experience the system live:  
👉 **[EV-Safety System Web App](https://ev-safety-system-5w5ik8ftvztrpk4shuic7c.streamlit.app/)** 👈

## 📌 Problem Statement

EV charging infrastructure is critical for electric vehicle adoption. Unexpected charger failures lead to:
- **Customer dissatisfaction** due to unavailable chargers
- **High repair costs** from catastrophic failures
- **Revenue loss** for charging station operators

This system predicts failures *before* they happen, enabling timely maintenance.

## 🧠 Solution Overview

An end-to-end machine learning pipeline that analyzes operational data from EV chargers to predict failures with **99% accuracy** and **zero missed failures**.

### How It Works

1. **Data Processing** – Clean, balance, and engineer features from charger logs.
2. **Model Training** – Random Forest classifier achieves 99% accuracy, 0.9999 AUC‑ROC.
3. **Prediction** – Real-time risk scoring for individual chargers.
4. **Actionable Alerts** – Color‑coded recommendations from “No action” to “Immediate maintenance”.

## 📊 Key Results

| Metric               | Value    |
|----------------------|----------|
| **Accuracy**         | 99.0%    |
| **AUC‑ROC**          | 0.9999   |
| **True Positives**   | 997 / 997 (all failures caught) |
| **False Negatives**  | 0        |
| **False Positives**  | 20 (minimal false alarms) |

## 🛠️ Tech Stack

| Area            | Technologies |
|----------------|--------------|
| Language       | Python 3.13  |
| ML Framework   | Scikit‑learn (Random Forest) |
| Data Handling  | Pandas, NumPy |
| Visualization  | Matplotlib, Seaborn |
| Deployment     | Streamlit |
| Development    | Jupyter Notebook |

## 🏗️ Project Structure
