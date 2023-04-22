f = 1
b = int(input())
for i in range(1, b+1):
    # f = f * i
    f *= i  # сокращенный оператор присваивания
print(f'{b}! = {f}')
