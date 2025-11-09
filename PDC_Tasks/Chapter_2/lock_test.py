# lock_test.py
import threading
import time
from matrix_mul import do_something

lock = threading.Lock()
results = []

def worker(id, count):
    start = time.time()
    value = do_something(count)   # CPU-bound matrix multiplication
    duration = time.time() - start

    # protect shared results with a lock
    with lock:
        results.append((id, value, duration))
        print(f"[Lock] Worker {id} appended result (time={duration:.3f}s)")

if __name__ == "__main__":
    threads = []
    num_workers = 5
    count = 3   # how many matrix multiplications each does (tune as needed)

    t0 = time.time()
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(i, count))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll workers done (Lock). Total time:", time.time() - t0)
    print("Results:", results)
