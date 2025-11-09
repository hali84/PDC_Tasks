# communicating_with_pipe.py
import multiprocessing
from matrix_mul import do_something

def worker_task(pipe_conn, count):
    result = do_something(count)
    pipe_conn.send(result)
    pipe_conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    
    process = multiprocessing.Process(target=worker_task, args=(child_conn, 3))
    process.start()

    print("⏳ Waiting for result from pipe...")
    result = parent_conn.recv()
    print(f"✅ Result received from pipe: {result}")

    process.join()
