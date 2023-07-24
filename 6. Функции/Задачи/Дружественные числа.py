def sum_divs(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

a = int(input())
b = int(input())
if sum_divs(a) == b and sum_divs(b) == a:
    print("YES")
else:
    print("NO")
