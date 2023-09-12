s = input()
last = len(s) % 10
for c in s:
    if c == s[last]:
        s[last] = s[last - 1]
    print('YES')
else:
    print('NO')