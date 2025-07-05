# Author: Syed Mohammad Askari Abidi

import psutil
import joblib
import time
from datetime import datetime

# Load the trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def get_live_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_io_counters()
    read_bytes = disk.read_bytes
    write_bytes = disk.write_bytes
    return [[cpu, memory, read_bytes, write_bytes]]

print("🚦 Real-time Anomaly Detector Running...\nPress Ctrl+C to stop.\n")

try:
    while True:
        metrics = get_live_metrics()
        scaled = scaler.transform(metrics)
        prediction = model.predict(scaled)[0]
        status = "🚨 ANOMALY" if prediction == 1 else "✅ Normal"

        print(f"[{datetime.now().strftime('%H:%M:%S')}] CPU: {metrics[0][0]}% | Mem: {metrics[0][1]}% → {status}")
except KeyboardInterrupt:
    print("\n🛑 Detection stopped.")
