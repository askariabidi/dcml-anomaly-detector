# Author: Syed Mohammad Askari Abidi

import threading
import time

def cpu_spike(duration=10):
    print("[INFO] Simulating CPU spike...")
    def _burn():
        end = time.time() + duration
        while time.time() < end:
            pass  # Burn CPU
    for _ in range(4):  # Adjust number for more/less load
        threading.Thread(target=_burn).start()

def memory_spike(duration=10):
    print("[INFO] Simulating memory overload...")
    junk = []
    end = time.time() + duration
    while time.time() < end:
        junk.append(' ' * 10_000_000)  # Allocate 10MB repeatedly
        time.sleep(0.1)

def disk_burst(duration=10):
    print("[INFO] Simulating disk write burst...")
    with open("temp_burst_file.txt", "w") as f:
        end = time.time() + duration
        while time.time() < end:
            f.write("A" * 10_000_000)  # Write 10MB at a time
            f.flush()
    print("[INFO] Cleaning up temporary file.")
    try:
        import os
        os.remove("temp_burst_file.txt")
    except:
        pass

if __name__ == "__main__":
    print("Choose anomaly to simulate:")
    print("1 - CPU spike")
    print("2 - Memory overload")
    print("3 - Disk burst")
    choice = input("Enter 1/2/3: ")

    if choice == "1":
        cpu_spike()
    elif choice == "2":
        memory_spike()
    elif choice == "3":
        disk_burst()
    else:
        print("Invalid choice.")
