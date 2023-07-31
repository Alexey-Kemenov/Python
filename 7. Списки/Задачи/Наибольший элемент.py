numbers = list(map(int, input().split()))
max = 0

for i in range(0, len(numbers), 1):
    if numbers[i] > numbers[max]:
         max = i

print(f"{numbers[max]}  {max}")
