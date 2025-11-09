# killing_processes.py
import multiprocessing
import time
from matrix_mul import do_something

def long_task():
    print("🚀 Process started... doing heavy matrix multiplication")
    do_something(10)  # Large workload
    print("✅ Task finished successfully!")

if __name__ == "__main__":
    p = multiprocessing.Process(target=long_task)

    p.start()
    p.join(timeout=2)  # wait 2 seconds only

    if p.is_alive():
        print("⛔ Timeout reached! Killing the process...")
        p.terminate()
        p.join()

    print("✅ Process terminated safely.")
