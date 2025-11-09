# semaphore_test.py
import threading
import time
from matrix_mul import do_something

# allow at most 2 threads to run matrix work at the same time
sem = threading.Semaphore(2)
results = []

def worker(id, count):
    print(f"[Semaphore] Worker {id} waiting for semaphore...")
    sem.acquire()
    try:
        print(f"[Semaphore] Worker {id} START")
        start = time.time()
        val = do_something(count)
        dur = time.time() - start
        results.append((id, val, dur))
        print(f"[Semaphore] Worker {id} DONE (time={dur:.3f}s)")
    finally:
        sem.release()

if __name__ == "__main__":
    threads = []
    for i in range(6):
        t = threading.Thread(target=worker, args=(i, 2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll workers done (Semaphore). Results count:", len(results))
