from multiprocessing import Pool
from matrix_mul import do_something

def compute(count):
    result = do_something(count)
    return f"Task Count={count} → Result={result}"

if __name__ == "__main__":
    counts = [1, 2, 3, 4, 5]  # 5 tasks

    with Pool(processes=3) as pool:  # 3 workers
        results = pool.map(compute, counts)

    print("=== Pool Results ===")
    for r in results:
        print(r)

    print("✅ Process Pool computation completed!")
