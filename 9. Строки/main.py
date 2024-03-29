"""
    Строки
    Строка - последовательность символов (коллекция), заключённых в одинарные или двойные кавычки.
    Строка НЕИЗМЕНЯЕМАЯ структура в Python!!!!!!!

    Обращение к строке происходит также, как и к спискам.

    Для вывода невидимых или особых символов используют esc-последовательности:
        \t - табуляция
        \n - перенос строки
        \\ - символ '\'

    Строку можно умножать на число. Результатом будет являться строка продублированная n раз.

    Для поиска подстроки в строке можно использовать оператор in.

    Функции
    isalpha() - функция, определяет, состоит ли строка только из алфавитных символов
    isdigit() - функция, определяет, состоит ли строка только из цифр
    isnumeric() - функция, определяет, является ли строка числом

    startswith(<str>) - функция, определяет, начинается ли строка с подстроки str
    endswith(<str>) - функция, определяет, оканчивается ли строка подстрокой str

    upper(), lower() - функции, возвращающие строку в верхнем или нижнем регистре

    lstrip(), rstrip(), strip() - функции удаления пробельных символов из начала, конца или с обеих сторон строки

    find(<str>, [start], [end]) - функция, возвращающая индекс подстроки str в строке. Если подстрока не найдена, возвращается -1
                                  Необязательные параметры: start - индекс начала поиска, end - индекс конца поиска
    replace(old, new, [count]) - функция, возвращающая строку, в которой подстрока old заменена строкой new.
                                 Необязательный параметр count - максимальное кол-во замен, которое разрешено произвести функции
    split([delimiter]) - функция, разбивающая строку на подстроки используя разделитель (по-умолчанию - пробел)
                         Функция возвращает массив строк.
    join(strs) - функция, объединяющая строки в массиве строк strs в одну строку, используя разделителем исходную строку
                 Пример: '-'.join(['a', 'b', 'c'])d
                 Результат работы функции: 'a-b-c'
    count(<str>, [start], [end]) - функция, определяет кол-во вхождений подстроки str в строку.
                                   Необязательные параметры: start - индекс начала поиска, end - индекс конца поиска
"""

# Неизменяемость строк
s = 'hello'
print(s)
s[1] = 'k' # Ошибка!!!
print(s)
# --------------------
