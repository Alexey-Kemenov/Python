def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())
count = 0
num = 2
while count < N:
    if is_prime(num):
        print(f"{num}", end=" ")
        count += 1
    num += 1
