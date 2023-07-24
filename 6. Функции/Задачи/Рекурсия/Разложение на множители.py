def prime_div(n, b):
    if n > 1:
        if n % b == 0:
            print(b)
            prime_div(n // b, b)
        else:
            prime_div(n, b + 1)


prime_div(10, 2 )
