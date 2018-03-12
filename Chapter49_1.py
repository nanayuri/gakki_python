import math
total = 0


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(max_num):
    number = 0
    while number < max_num:
        if is_prime(number):
            yield number
        number += 1


for each in get_primes(200000000):
    total += each

print(total)


