def encode(n):
    for i in n:
        a = alph.find(i)
        b = a + step
    return b
def decode(n):
    for i in n:
        a = alph.find(i)
        d = a - step
    return d


alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
step = 3
s = input()
y = input()
shifr = ''
original = ''
e = 0
o = 0
for c in s:
    if encode(c):
        e = encode(c)
        shifr += alph[e]
print(shifr)

for j in y:
    if decode(j):
        o = decode(j)
        original -= alph[o]
print(original)
