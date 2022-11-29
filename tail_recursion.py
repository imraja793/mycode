def fact(n, a):
    if n < 2:
        return a
    else:
        return fact(n-1, n*a)

print(fact(2,1), "got the answer")


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)
print(factorial(5))