s = input()
word = ''
s = s.split()
for c in s:
    if len(c) > len(word):
        word = c
print(word)
print(len(word))


