a = int(input())
f1 = 0
f2 = 1
b = 0
while b < a:
    f1, f2 = f2, f1 + f2
    b += 1
print(f1)
