numbers = list(map(int, input().split()))
a = 1
for i in range(0, len(numbers)):
    if i < 2:
        if numbers[i] != numbers[i + 1]:
            a += 1
    if i > 2:
        if numbers[i - 1] != numbers[i]:
            a += 1

print(a)
