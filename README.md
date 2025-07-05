# 📊 DCML 2024–2025 – Real-Time Anomaly Detector for Laptops

This repository contains the implementation of a **real-time anomaly detection system** for laptops and standalone workstations. The project was developed as part of the **Data Collection and Machine Learning (DCML)** course at the University of Florence.

---

## 🎯 Project Objective

To monitor system performance metrics (CPU, memory, I/O) in real-time, train a machine learning model to distinguish between normal and anomalous behavior, and use the model to detect anomalies live as the system runs.

---

## 🧱 Project Structure

| File/Folder       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `monitor.py`      | Monitors CPU, memory, read/write bytes and logs data to `dataset.csv`      |
| `injector.py`     | Simulates CPU or memory spikes to generate anomalies                       |
| `train_model.py`  | Trains a binary classification model (`normal` vs `anomaly`)               |
| `predictor.py`    | Runs the saved model in real-time to detect anomalies                      |
| `dataset.csv`     | Collected and labeled training data (normal + injected anomalies)          |
| `model.pkl`       | Saved trained machine learning model                                       |
| `scaler.pkl`      | Saved standard scaler for real-time data normalization                    |
| `README.md`       | This project overview and instructions                                     |
| `report.pdf`      | Methodology and technical explanation (submitted for course evaluation)   |
| `demo.mp4` / `demo.txt` | Demo video or YouTube link to the 5-minute recording                  |
| `report-assets/`  | Optional screenshots/graphs for the report                                 |

---

## 🛠️ Technologies Used

- Python 3.12
- `psutil` (system monitoring)
- `scikit-learn` (ML model training)
- `pandas` and `numpy` (data handling)
- `joblib` (model saving/loading)
- Visual Studio Code (development environment)

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/askariabidi/dcml-anomaly-detector.git
cd dcml-anomaly-detector

python -m venv venv
venv\Scripts\activate  # On Windows

pip install psutil pandas scikit-learn joblib matplotlib seaborn

python monitor.py
# Let it run for a few minutes while you use your computer normally
# Press Ctrl+C to stop and save dataset.csv

python injector.py
# Choose a stress test (CPU or memory)

Label the Data
Open dataset.csv in Excel or a CSV editor
→ Label "anomaly" for time periods during stress injection

python train_model.py
# Outputs model.pkl and scaler.pkl

python predictor.py
# Run injector again to simulate anomaly in real time


