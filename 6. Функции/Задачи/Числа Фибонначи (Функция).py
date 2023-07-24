def fibonacci(n):
    f1 = 0
    f2 = 1
    b = 0
    while b < n:
        f1, f2 = f2, f1 + f2
        b += 1

    return f1


a = int(input())
print(fibonacci(a))
