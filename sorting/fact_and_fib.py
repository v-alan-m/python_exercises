def fact(n):
	"""Calculate the factorial of the provided value."""
	if n < 2:
		return 1

	return n * fact(n - 1)


def fib(n):
	"""Calculate the nth Fibonacci number."""
	if n < 2:
		return 1

	return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
	print(" n\t                 n!\tfib(n)")
	for n in range(20):
		print("{:2d}\t{:18d}\t{:4d}".format(n, fact(n), fib(n)))
