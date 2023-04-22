n = int(input())
pos = 0
neg = 0
zero = 0
for i in range(n):
    a = int(input())
    if a > 0:
        pos += 1
    if a == 0:
        zero += 1
    if a < 0:
        neg += 1
print(f"Положительных: {pos}")
print(f"Отрицательных: {neg}")
print(f"Нулей: {zero}")
