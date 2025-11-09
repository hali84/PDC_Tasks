from multiprocessing import Process
from matrix_mul import do_something

class MatrixMultiplicationProcess(Process):
    def __init__(self, count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = count

    def run(self):
        print(f"[START] {self.name} with count={self.count}")
        result = do_something(self.count)
        print(f"[DONE] {self.name} → Result: {result}")

if __name__ == "__main__":
    workers = [
        MatrixMultiplicationProcess(1, name="SubclassWorker-1"),
        MatrixMultiplicationProcess(2, name="SubclassWorker-2"),
        MatrixMultiplicationProcess(3, name="SubclassWorker-3")
    ]

    for w in workers:
        w.start()

    for w in workers:
        w.join()

    print("✅ Subclass-based workers completed!")
