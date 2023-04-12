"""
    Цикл for
    Цикл, перебирающий коллекции
"""
# range(<n>) - числа от 0 до n не включительно
# range(<a>, <b>) - числа от a до b не включительно
# range(<a>, <b>, <s>) - числа от a до b с шагом s
print(list( range(10, 50, 3) ))

for i in range(10):
    print(i)

# Перебирает символы в строке
for c in 'HELLO':
    print(c)
