# Author: Syed Mohammad Askari Abidi

import psutil
import csv
import time
from datetime import datetime

OUTPUT_FILE = "dataset.csv"
SAMPLE_INTERVAL = 1  # seconds

def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_io_counters()
    read_bytes = disk.read_bytes
    write_bytes = disk.write_bytes
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [timestamp, cpu, memory, read_bytes, write_bytes]

def start_monitor():
    print(f"[INFO] Monitoring started. Saving to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "cpu_percent", "memory_percent", "read_bytes", "write_bytes", "label"])
        try:
            while True:
                row = get_metrics()
                row.append("normal")
                writer.writerow(row)
                print(row)
                time.sleep(SAMPLE_INTERVAL)
        except KeyboardInterrupt:
            print("\n[INFO] Monitoring stopped by user.")

if __name__ == "__main__":
    start_monitor()
