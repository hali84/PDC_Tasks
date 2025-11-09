# event_test.py
import threading
import time
from matrix_mul import do_something

start_event = threading.Event()
results = []

def worker(id, count):
    print(f"[Event] Worker {id} waiting for start event...")
    start_event.wait()   # blocks until event is set
    start = time.time()
    val = do_something(count)
    dur = time.time() - start
    results.append((id, val, dur))
    print(f"[Event] Worker {id} finished (time={dur:.3f}s)")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i, 3))
        threads.append(t)
        t.start()

    print("Main thread sleeping 2s then setting event (simulate setup)...")
    time.sleep(2)
    start_event.set()   # all waiting threads start simultaneously

    for t in threads:
        t.join()

    print("\nAll workers done (Event). Results:", results)
