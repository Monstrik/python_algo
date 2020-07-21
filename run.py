# sort



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_loop(n):
    if n == 0:
        return 1
    f = 1
    i = 0

    while (i < n):
        i += 1
        f = f * i
    return f
print(" -- Start -- ")


print(factorial(998))
print(factorial_loop(7))
print(" -- Finish -- ")
