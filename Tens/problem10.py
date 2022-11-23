# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# from helpers import is_prime

# primes = []
# for i in range(100):
#     if is_prime(i):
#         primes.append(i)

# #print(primes)
# sum_primes = 0
# for p in primes:
#     sum_primes = sum_primes + int(p)

# print(sum_primes)

# New method from reading the docs advice

from helpers import SieveOfEratosthenes

primes = SieveOfEratosthenes(2000000)
sum_primes = 0
for p in primes:
    sum_primes = sum_primes + int(p)
print(sum_primes)