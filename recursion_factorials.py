def fact(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input to factorial must be a positive integer!")
    if n < 2:
        return 1
    return n * fact(n - 1)