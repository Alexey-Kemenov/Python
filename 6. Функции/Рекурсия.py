"""
    Рекурсия - явление, при котором функция вызывает внутри себя саму.
    Можно сказать, что рекурсия выступает в роли цикла.
    - В рекурсии есть 2 части: Прямой ход, Обратный ход
    Прямой ход заканчивается, как только функция первый раз не вызвала себя.
    - Между вызовами функции не сохраняются переменные, объявленные внутри неё.
    Для передачи значений между вызовами следует использовать параметры.
"""

# Вывести последовательность от 1 до n
def print_seq(n):
    if n != 0:
        print_seq(n - 1)
        print(n, end=' ')

print_seq(10)

# --- --- --- ---
print()
# Сумма элементов последовательности от 0 до n
def sum_seq(n):
    if n == 0:
        return 0
    return sum_seq(n - 1) + n

print(sum_seq(10))