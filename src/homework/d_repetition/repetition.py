#
# src/homework/d_repetition/repetition.py

def get_factorial(n):
    if n == 0:
        return 1
    else:
        return n * get_factorial(n - 1)

def sum_odd_numbers(n):
    return sum([i for i in range(1, n + 1) if i % 2 != 0])
