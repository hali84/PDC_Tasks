# rlock_test.py
import threading
import time
from matrix_mul import do_something

rlock = threading.RLock()
results = []

def nested_work(id, count, depth):
    """
    shows that same thread can re-acquire the lock recursively
    """
    with rlock:
        if depth > 0:
            # re-enter: safe because this is RLock and same thread
            nested_work(id, count, depth - 1)
        else:
            # do the heavy computation at the innermost level
            start = time.time()
            value = do_something(count)
            duration = time.time() - start
            results.append((id, value, duration))
            print(f"\n[RLock] Worker {id} finished (time={duration:.3f}s)")

def worker(id):
    nested_work(id, 2, 2)  # depth 2 recursion

if __name__ == "__main__":
    threads = []
    for i in range(4):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll workers done (RLock). Results:", results)
