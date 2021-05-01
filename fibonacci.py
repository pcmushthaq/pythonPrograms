def fiboIterative(n: int):
    initial = [0, 1]
    for i in range(2, n+1):
        initial.append(initial[i-1]+initial[i-2])
    print(initial)
    return initial[n]


def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1)+fibonacci(n-2)


print(fiboIterative(12))
print(fibonacci(12))
