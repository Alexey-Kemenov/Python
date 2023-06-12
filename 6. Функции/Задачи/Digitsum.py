def   digit_sum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


a = int(input())
b = int(input())
s = int(input())
while a < b:

    if digit_sum(a) == s:
        print(a)
    a += 1
