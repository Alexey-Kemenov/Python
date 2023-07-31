numbers = list(map(int, input().split()))
x = int(input())
a = 0
for i in range(0, len(numbers)):
    if numbers[i] >= x:
        a += 1
print(a)