def check_prime(number):
    flag = True
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return flag


def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number


primes = Primes(10)
for x in primes:
    print(x)

primes = (i for i in range(2, 100) if check_prime(i))
print(primes, "dkmdkkdf")


def fgenerator_fun():
    i = 1
    while i:
        yield i * i
        i += 1


for num in fgenerator_fun():
    if num > 100:
        break
    print(num)

