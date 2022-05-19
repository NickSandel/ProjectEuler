def prime_factors(n):
    """Returns a dictionary of prime: order. For example 100 (prime factors 2x2x5x5) would return {2: 2, 5:2}"""
    if n == 1:
        return {}

    p = 2
    factors = {}

    while n >= p * p:
        if n % p == 0:
            factors.setdefault(p, 0) # Adds factor if it's not already there
            factors[p] += 1 # Increments count of factor found
            n = n / p # Prime factorization. Each whole (composite) number has only 1 unique set of prime numbers which make it up. All other factors can be made from these primes
                      # Therefore if you start at the lowest prime and walk up as you reduce n by p the lowest factor you will find will always be a prime number as they're always the lowest base factors
        else:
            # 2 is the first prime, if on 2 go to 3 else skip 2 so even numbers are ignored as they can't be primes
            if p <= 2:
                p += 1
            else:
                p += 2

    n = int(n)
    factors.setdefault(n, 0)
    factors[n] += 1

    return factors


def is_palindrome(value):
    if str(value) == str(value)[::-1]:
        return True
    else:
        return False
    