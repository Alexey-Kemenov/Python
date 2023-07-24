def binary_code(n):
    if n != 0:
        binary_code(n // 2)
        print(n % 2, end="")
        


binary_code(6)

"""
a = int(input())
b = 0
while a != 0:
    b = a % 2
    print(b, end="")
    a //= 2
"""
