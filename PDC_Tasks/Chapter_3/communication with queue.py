# communicating_with_queue.py
import multiprocessing
from matrix_mul import do_something

def worker_task(task_queue, result_queue):
    while not task_queue.empty():
        count = task_queue.get()
        res = do_something(count)
        result_queue.put((count, res))
        task_queue.task_done()

if __name__ == "__main__":
    task_queue = multiprocessing.JoinableQueue()
    result_queue = multiprocessing.Queue()

    # Add different workloads
    for i in [2, 3, 4]:
        task_queue.put(i)

    processes = []
    for _ in range(2):
        p = multiprocessing.Process(target=worker_task, args=(task_queue, result_queue))
        processes.append(p)
        p.start()

    task_queue.join()

    print("\n✅ Results from Queue:")
    while not result_queue.empty():
        count, res = result_queue.get()
        print(f"Matrix multiplied {count} times → Result: {res}")

    for p in processes:
        p.join()
