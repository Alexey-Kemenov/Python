s = input()
alph = '0123456789ABCDEF'
i = 0
n = len(s)
x = 0
for c in s:
    x += (s[c] * 16 ** n)
i += 1
n -= 1

print(x)
