import threading
import time
from matrix_mul import do_something

# Barrier waits until all threads reach this point
barrier = threading.Barrier(5)

def worker():
    print(f"> Thread reached barrier")
    barrier.wait()  # sync point
    start = time.time()
    result = do_something(5)
    duration = time.time() - start
    print(f"✔ Thread done. Result={result}, Time={duration:.4f}s")

if __name__ == "__main__":
    threads = []

    start_all = time.time()

    for _ in range(5):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\nTotal Execution Time: {time.time() - start_all:.4f}s")
