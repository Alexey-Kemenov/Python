s = input()
s = s.replace(' ', '')
print('YES' if s == s[::-1] else 'NO')
