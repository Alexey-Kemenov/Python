def is_prime(n, a):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if a >= n:
        return True
    if n % a == 0:
        return False

    return is_prime(n, a + 1)


#print("Yes" if is_prime(2, 2) else "No")

for i in range(0, 100):
    if is_prime(i, 2):
        print(i)


