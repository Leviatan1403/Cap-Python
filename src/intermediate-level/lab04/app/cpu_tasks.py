from concurrent.futures import ProcessPoolExecutor


def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def calculate():

    numbers = [32, 33, 34, 35]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(fibonacci, numbers))

    return results
