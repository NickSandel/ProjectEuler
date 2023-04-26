# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1**2
# 15 = 7 + 2×2**2
# 21 = 3 + 2×3**2
# 25 = 7 + 2×3**2
# 27 = 19 + 2×2**2
# 33 = 31 + 2×1**2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# Things I know:
# All composite numbers decompose into primes
# I think I've done something before figuring out which primes they decompose into
# The small ones should be easy to figure out

from common.helpers import prime_factors, is_prime, SieveOfEratosthenes

# Generate a bunch of numbers which meet the formula: prime + 2xn**2
# Then find an odd composite which is not in this list?

primes_1000 = SieveOfEratosthenes(10000)

double_squares = set()
for i in range(1,500):
    double_squares.add(2 * (i**2))

combined_tests = set()
for prime in primes_1000:
    for double_square in double_squares:
        combined_tests.add(prime + double_square)

for i in range(3,40000, 2):
    if not is_prime(i):
        if not i in combined_tests:
            print(f"{i} does not pass test")
            break