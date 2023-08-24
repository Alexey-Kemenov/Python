numbers = list(map(int, input().split()))
posmax = 0
posmin = 0
for i in range(0, len(numbers)):
    if numbers[i] > numbers[posmax]:
        posmax = i
    if numbers[i] < numbers[posmin]:
        posmin = i
numbers[posmax], numbers[posmin] = numbers[posmin], numbers[posmax]

print(numbers)
