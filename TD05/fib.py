import math
import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit

def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_iter(n):
    result = [0, 1]
    for _ in range(n):
        result[0], result[1] = result[1], result[0] + result[1]
    return result[0]

def fibonacci_mat(n):
    initial_vector = np.array([1, 0])
    linear_transform = np.array([[1, 1], [1, 0]])
    iteration_vector = np.linalg.matrix_power(linear_transform, n) @ initial_vector
    return iteration_vector[0]

def measure(func, values, number=100):
    m = []
    for i in values :
        m.append(timeit(lambda : func(i), number=number))
    return m

if __name__ == "__main__":
    sample = list(range(1, 30))
    rec = measure(fibonacci_rec, sample)
    iter = measure(fibonacci_iter, sample)
    mat = measure(fibonacci_mat, sample)

    plt.plot(sample, rec, "--", label="Recursive", color="red")
    plt.plot(sample, iter, "-.", label="Iterative", color="blue")
    plt.plot(sample, mat, ".", label="Matrix", color="green")
    plt.legend()
    plt.yscale("log")
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.title("Fibonacci Execution Time")
    plt.show()
