numbers = list(map(int, input().split()))
a = 1
for i in range(0, len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        a += 1

print(a)
