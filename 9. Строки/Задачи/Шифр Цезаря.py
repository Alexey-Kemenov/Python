"""
    Шифр Цезаря
    Написать программу, которая кодирует в тексте русские буквы (в любом регистре).
    Любые другие символы остаются без изменения.
    В программе должно быть две функции: encode и decode, которые принимают строку и ключ, возвращают закодированную
    или раскодированную строку соответственно.
    Сделать подобие меню, в котором пользователь выбирает какое действие ему надо сделать с вводимым текстом.

    TODO: 1. В функциях не используются глобальные переменные
          2.
"""


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

s = input()
y = input()
step = 3

shifr = ''
original = ''
e = 0
o = 0
for c in s:
    if encode(c):
        e = encode(c)
        shifr += alph[e]
print(shifr)

"""for j in y:
    if decode(j):
        o = decode(j)
        original -= alph[o]
print(original)"""
