def decimal_code(n, count):
    if n == 0:
        return 0
    return decimal_code(n // 10, count + 1) + ((n % 10) * 2 ** count)


print(decimal_code(100101, 0))
