def reverse(a, b):
    if a == 0:
        return b
    else:
        return reverse(a // 10, b * 10 + a % 10)


print(reverse(21, 0))


def reverse2(a):
    if a == 0:
        return a
    else:
        return (a % 10 * 10) + reverse2(a // 10)


print(reverse2(179))

"""   
            a = int(input())
            b = 0
            num = 0
            while a > 0:
                num = a % 10
                b = b * 10 + num
                a //= 10
                print(b)
"""
