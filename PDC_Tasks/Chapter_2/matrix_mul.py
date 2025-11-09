import random

def do_something(count):
    size = 20  # keep small for testing synchronization
    A = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
    B = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

    for _ in range(count):
        result = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i][j] += A[i][k] * B[k][j]

    return result[0][0]  # return something small
