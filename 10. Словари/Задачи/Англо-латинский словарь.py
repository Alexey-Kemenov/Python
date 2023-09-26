words = dict()
n = int(input())
count = 0
while n > 0:
    s = input().replace("-", "").replace(',', '').split()
    n -= 1
    for word in s[1:]:
        if word in words:
            words[word].append(s[0])
        else:
            words[word] = [s[0]]

words = dict(sorted(list(words.items())))

print(len(words))
for key, value in words.items():
    print(f'{key} - {", ".join(sorted(value))}')
