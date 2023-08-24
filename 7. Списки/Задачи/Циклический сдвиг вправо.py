numbers = list(map(int, input().split()))
n = numbers.pop()
numbers.insert(0, n)

print(numbers)
