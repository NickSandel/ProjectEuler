from math import sqrt
from math import floor


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

def is_prime(n: int):
    # If n is negative flip to positive
    if n < 0:
        n = n * - 1
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f = f + 6
        return True

# Nabbed offline from:
# https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    primes = set()
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            primes.add(p)
    return primes

class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

def is_pandigital(number: str):
    digits = sorted(number)
    for i, d in enumerate(digits):
        if d != str(i + 1):
            return False
    return True

def is_pentagonal(n: int):
    # A number is pentagonal if it can be calculated with the formula: Pn=n(3n−1)/2
    # So we can solve for n and see if it's an integer
    n = (1 + sqrt(1 + 24*n))/6
    return n.is_integer()

def is_triangular(n: int):
    # Wikipedia gives me this formula for checking if a number is triangular:
    n = ((sqrt(1 + 8*n))-1)/2
    return n.is_integer()

def is_permutation(item:int, match:int):
    return sorted(str(item)) == sorted(str(match))
