def is_friends(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


a = int(input())
b = int(input())
for i in range(a, b):
    for j in range(i+1, b):
        if is_friends(i) == j and is_friends(j) == i:
            print(f"{(i, j)}", end=" ")




