n = int(input())
m = 0
pre = 0
count = 0
while n != 0:
    if pre == n:
        count += 1
        m = max(m, count)
    else:

        count = 0
    pre = n
    n = int(input())
print(m+1)
