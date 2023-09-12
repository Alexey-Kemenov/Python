s = input()
count = 0
result = ''
for c in s:
    if c == 'a':
        result += 'b'
        count += 1
    else:
        result += c
print(result)
print(count)
