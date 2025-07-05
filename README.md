# 📊 Real-Time Anomaly Detector for Laptops

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
| `scaler.pkl`      | Saved standard scaler for real-time data normalization                     |
| `README.md`       | This project overview and instructions                                     |
| `report.pdf`      | Methodology and technical explanation (submitted for course evaluation)    |
| `demo.txt`        | Demo video or YouTube link to the 5-minute recording                       |
| `report-assets/`  | Optional screenshots/graphs for the report                                 |

---

## 🛠️ Technologies Used

- Python 3.12
- `psutil` – for system monitoring
- `scikit-learn` – for machine learning
- `pandas`, `numpy` – for data manipulation
- `joblib` – for saving/loading ML models
- Visual Studio Code – as the development environment

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/askariabidi/dcml-anomaly-detector.git
cd dcml-anomaly-detector
```

### 2. Set Up the Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install psutil pandas scikit-learn joblib matplotlib seaborn
```

### 4. Collect Normal System Data

```bash
python monitor.py
```

- Let it run for a few minutes while you use your computer normally  
- Press `Ctrl+C` to stop and save the file as `dataset.csv`

### 5. Simulate Anomalies

```bash
python injector.py
```

- Choose option `1` or `2` to simulate CPU or memory overload

### 6. Label the Data

- Open `dataset.csv` in Excel or a CSV editor
- Label `"anomaly"` for time periods during which the injector was running
- Save the labeled file

### 7. Train the Machine Learning Model

```bash
python train_model.py
```

- This generates and saves `model.pkl` and `scaler.pkl`

### 8. Run Real-Time Anomaly Detection

```bash
python predictor.py
```

- While it runs, re-run `injector.py` in a separate terminal to simulate an anomaly
- Watch the terminal output — it will print 🚨 `ANOMALY` if detected

---

## 📽️ Demo Video

🎥 You can watch the full demo here:  
🔗 [YouTube Demo Link](https://youtu.be/y3zZkiE3Odk)

---

## 🧑‍🎓 Author

**Name**: Syed Mohammad Askari Abidi  
**University**: University of Florence  
**Program**: Master's in Software: Science and Technology  
**Course**: B032430 (B255) - DATA COLLECTION AND MACHINE LEARNING FOR CRITICAL CYBER-PHYSICAL SYSTEMS
**Academic Year**: 2024–2025  

---

## 📝 License

This project is submitted for academic purposes. For reuse or collaboration, please contact the author.
