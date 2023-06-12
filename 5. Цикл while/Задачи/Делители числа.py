n = int(input())
i = 1
sum = 0
while i <= n:
    if n % i == 0:
        sum = sum + 1
    i = i + 1
print(sum)
