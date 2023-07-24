def max_num(n, max_digit):
    if n % 10 < max_digit:
        return max_digit

    if max_digit < (n % 10):
        max_digit = n % 10

    return max_num(n // 10, max_digit)


print(max_num(12345432, 0))
"""
n = int(input())
max_digit = 0
while n > 0:
    if max_digit < n % 10:
        max_digit = n % 10
    n = n // 10
print(max_digit)
"""
