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

def measure(func, values, number=100):
    m = []
    for i in values :
        m.append(timeit(lambda : func(i), number=number))
    return m

if __name__ == "__main__":
    sample = [1, 2, 3, 5, 10, 20, 25]
    rec = measure(fibonacci_rec, sample)
    iter = measure(fibonacci_iter, sample)

    plt.plot(sample, rec, "--", label="Recursive", color="red")
    plt.plot(sample, iter, "-.", label="Iterative", color="blue")
    plt.legend()
    plt.yscale("log")
    plt.xlabel("Input Size")
    plt.ylabel("Time (s)")
    plt.title("Execution Time")
    plt.show()
