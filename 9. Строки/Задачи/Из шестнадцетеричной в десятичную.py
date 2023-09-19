s = input()
x = ''
i = 0
n = len(s)
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
for c in s:

        x += (s[c] * 16 ** n)
i += 1
n -= 1

print(x)
