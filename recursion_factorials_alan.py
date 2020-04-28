def fact(n)
    # Base case
    if n == 0
        return 1
    elif n  0
        raise ValueError(Please make input a positive integer)
    # Recursion
    return n  fact(n-1)

if __name__ == "__main__":
	fact(10)