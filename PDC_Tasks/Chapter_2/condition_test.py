# condition_test.py
import threading
import time
from matrix_mul import do_something

cond = threading.Condition()
results = []
TARGET = 4

def worker(id, count):
    val = do_something(count)
    with cond:
        results.append((id, val))
        print(f"[Condition] Worker {id} appended result ({len(results)}/{TARGET})")
        cond.notify_all()  # tell waiting thread(s) that something changed

def controller():
    with cond:
        while len(results) < TARGET:
            print(f"[Condition] Controller waiting, have {len(results)}/{TARGET}")
            cond.wait(timeout=5)  # waits until notify or timeout
        print("[Condition] Controller: target reached, processing results:", results)

if __name__ == "__main__":
    # start controller thread
    ctrl = threading.Thread(target=controller)
    ctrl.start()

    # start producer workers
    threads = []
    for i in range(TARGET):
        t = threading.Thread(target=worker, args=(i, 2))
        threads.append(t)
        t.start()
        time.sleep(0.5)  # stagger producers a bit

    for t in threads:
        t.join()
    ctrl.join()
    print("\nCondition demo finished.")
