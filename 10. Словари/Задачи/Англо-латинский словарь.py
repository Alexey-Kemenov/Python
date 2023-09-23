words = dict()
n = int(input())
count = 0
while n > 0:
    s = input()
    n -= 1
    s = s.replace("-", "")
    s = s.split()
    for c in s[1:]:
        words[c] = s[0]

for key, value in words.items():
    #if value != value:
        print(f'{key} - {value, value}')
    count += 1
    print(f'{key} - {value}')
print(count)