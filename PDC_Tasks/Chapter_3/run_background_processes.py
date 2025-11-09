# We use daemon=True for background matrix workers.
from multiprocessing import Process
from time import sleep
from matrix_mul import do_something

def background_task():
    print(f"[START] Daemon {Process().name}")
    do_something(1)
    print(f"[EXIT] Daemon {Process().name} (may not show if main ends early)")

if __name__ == "__main__":
    p = Process(target=background_task)
    p.daemon = True  # Important!!
    p.start()

    print("Main process doing some short task...")
    sleep(1)
    print("Main process exiting now!")
    # Daemon will be killed immediately if still running ✅
  