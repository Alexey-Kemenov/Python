n = int(input())
max = 0
i = 0
while n != 0:
    if n > max:
        max = n
        pos = i
    i = i + 1

    n = int(input())

print(f"позиция:{pos} max :{max}")
