"I dont fucking know, it's from some math video"
from time import time


def check_caboose(sieve):
    "The fuck is a caboose?"
    caboose_limit = len(sieve)
    for i in range(caboose_limit):
        if sieve[i]:
            caboose = True
            for j in range(1, i):
                testable = j * j - j + i
                if testable > caboose_limit:
                    break
                if not sieve[testable]:
                    caboose = False
                    break
            if caboose:
                print(i)


def sieve_of_atkin(limit):
    "Finds all prime numbers up to the limit"
    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False
        r += 1

        # Print primes
    return sieve


p1 = time()
LIMIT = 100000000
a = sieve_of_atkin(LIMIT)
p2 = time()
check_caboose(a)
p3 = time()
print(f"Sieving {round(p2-p1,3)}s")
print(f"Caboosing {round(p3-p2, 3)}s")
