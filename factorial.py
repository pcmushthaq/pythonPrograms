def factorialIterative(n: int):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorialIterative(5))
print(factorial(6))
