def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
        return True


class Primes:

    def __init__(self, max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()


primes = Primes(1000)
print(primes, "sdd")
print(primes)