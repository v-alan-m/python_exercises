# Create a recursive function
def fibonacci(n):
    # Base condition
    if n == 1 or n == 2:
        return 1
    # When n > 2, the function will run as recursive function
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        print('The input must be a positive integer')

if __name__ == "__main__":
    fibonacci(10)