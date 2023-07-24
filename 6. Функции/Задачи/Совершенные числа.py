def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

N = int(input())
num = 1
count = 0
while count < N:
    if is_perfect(num):
        print(f"{num}", end=" ")
        count += 1
    num += 1
