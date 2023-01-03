# Euler discovered the remarkable quadratic formula:
# n**2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n=40, 40**2 + 40 + 41 = 40(40+1) is divisible by 41, 
# and certainly when n=41, 41**2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n**2-72n+1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. 
# The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
# n**2 + an + b, where |a| and |b| <= 1000
# where |11| = 11 is the modulus/absolute value of n
# e.g. |11| = 11 and  |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
# starting with n=0.

# I guess start with the known and validating how many primes it produces
# n**2 + n + 41
from math import floor, sqrt
def is_prime(n):
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

n = 0
prime_count = 0
while n < 40:
    prime_test = (n**2) + n + 41
    if is_prime(prime_test):
        prime_count += 1
    else:
        print('Found a non prime')
        prime_count = 0
        break
    n += 1

print(prime_count)

def consecutive_primes_limit_from_quadratic(a, b):
    n = 0
    prime_count = 0
    while n < max((sqrt(b**2)), (sqrt(a**2))): #I like this trick to basically ignore the +/- if you square then square root you'll get the positive version
        prime_test = (n**2) + (a*n) + b
        if is_prime(prime_test):
            prime_count += 1
        else:
            break
        n += 1
    return prime_count

primes_41 = consecutive_primes_limit_from_quadratic(1, 41)
print(primes_41)

primes_minus41 = consecutive_primes_limit_from_quadratic(1, -41)
print(primes_minus41)

primes_second = consecutive_primes_limit_from_quadratic(-79, 1601)
print(primes_second)

# This seems to be working ok then so do I just iterate through the -1000 to +1000 range and look for the largest number coming out?
highest_ab = [0,0]
highest_count = 0
start = -1000
a = start
b_start = start
while a <= sqrt(start**2):
    b = b_start
    while b <= sqrt(start**2):
        prime_count = consecutive_primes_limit_from_quadratic(a, b)
        if prime_count > highest_count:
            highest_count = prime_count
            highest_ab = [a, b]
        b += 1
    a += 1

print(f"Highest number of primes is from pairing: {highest_ab} which had {highest_count} primes and the product of these is {highest_ab[0] * highest_ab[1]}")