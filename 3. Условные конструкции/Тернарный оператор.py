"""
    Тернарный оператор

    [<переменная> =] <если true> if <логическое выражение> else <если false>

    Замена
    if a > b:
        max = a
    else:
        max = b
"""

# Нахождение максимального значения

a = 8
b = 12

max = a if a > b else b

c = 48

# Сложный вариант с тремя переменными
max = (a if a > c else c) if a > b else (a if b > c else b)
