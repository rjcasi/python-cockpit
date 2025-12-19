#classic recursive Fibonacci — elegant, simple, and perfect for visualization.
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)