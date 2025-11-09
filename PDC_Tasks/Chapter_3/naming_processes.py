from multiprocessing import Process
from matrix_mul import do_something

def worker(count):
    process_name = f"Worker-{count}"
    print(f"[START] {process_name}")
    result = do_something(count)
    print(f"[DONE] {process_name} → Result: {result}")

if __name__ == "__main__":
    processes = []

    # Assign different counts to each process
    for count in [1, 2, 3]:
        p = Process(target=worker, args=(count,), name=f"MatrixWorker-{count}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("✅ All named processes completed!")
