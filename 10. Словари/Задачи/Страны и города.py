countries = dict()
n = int(input())
while n > 0:
    s = input().split()
    n -= 1
    for c in s[1:]:
        countries[c] = s[0]

m = int(input())
while m > 0:
    city = input()
    m -= 1
    print(countries[city])

