from multiprocessing import Process
from matrix_mul import do_something

def background_task():
    print(f"[START] Non-daemon {Process().name}")
    do_something(2)
    print(f"[DONE] Non-daemon {Process().name} finished matrix work ✅")

if __name__ == "__main__":
    p = Process(target=background_task)
    # p.daemon = False → Default
    p.start()

    print("Main will wait for background job ✅")
    p.join()
    print("Main process exits after background completes ✅")
