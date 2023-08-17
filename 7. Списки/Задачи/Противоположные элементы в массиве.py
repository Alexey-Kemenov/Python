numbers = list(map(int, input().split()))
for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if numbers[i] + numbers[j] == 0:
            print(i, end=' ')





