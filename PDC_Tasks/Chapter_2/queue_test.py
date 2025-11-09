# queue_test.py
import threading
import time
from queue import Queue
from matrix_mul import do_something

q = Queue()
results = []
NUM_CONSUMERS = 3

def producer():
    # put 6 tasks into queue
    for i in range(6):
        task_count = 2
        print(f"[Queue] Producer enqueuing task {i}")
        q.put((i, task_count))
    # send sentinel None for each consumer to stop
    for _ in range(NUM_CONSUMERS):
        q.put(None)

def consumer(cid):
    while True:
        item = q.get()
        if item is None:
            print(f"[Queue] Consumer {cid} got stop signal.")
            q.task_done()
            break
        task_id, count = item
        start = time.time()
        val = do_something(count)
        dur = time.time() - start
        results.append((cid, task_id, val, dur))
        print(f"[Queue] Consumer {cid} processed task {task_id} (time={dur:.3f}s)")
        q.task_done()

if __name__ == "__main__":
    # start consumers
    consumers = []
    for i in range(NUM_CONSUMERS):
        t = threading.Thread(target=consumer, args=(i,))
        t.start()
        consumers.append(t)

    # start producer
    prod = threading.Thread(target=producer)
    prod.start()
    prod.join()

    q.join()  # wait until all tasks marked done

    print("\nAll queue tasks processed. Results:", results)
    for c in consumers:
        c.join()
