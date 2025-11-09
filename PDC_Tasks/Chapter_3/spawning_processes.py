# We create multiple spawned workers for matrix computations.
from multiprocessing import Process, set_start_method
from matrix_mul import do_something

def worker(i):
    print(f"[SPAWN] Worker-{i} started")
    result = do_something(1)
    print(f"[DONE] Worker-{i} result: {result}")

if __name__ == "__main__":
    try:
        # Windows default = spawn. Unix default=fork, but we force spawn for consistency
        set_start_method("spawn")
    except RuntimeError:
        pass  # Method already set earlier

    workers = []
    for i in range(3):
        p = Process(target=worker, args=(i,))
        workers.append(p)
        p.start()

    for p in workers:
        p.join()

    print("✅ All spawned processes completed!")
