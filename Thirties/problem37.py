# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right
# , and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# Ok it says the ONLY 11 primes so there must be some upper limit but nothing is immediately obvious as to why. 
# There is one limitation I can clearly see which is that it can only begin and end with 3 and 7! 
# 2 is out because combined with any other number where it's on the end it can't be prime as is 5. 
# 1 isn't prime neither is 4,6,8,9
# For the mid digits they must all be odd otherwise they'll produce some non-prime as you truncate the number. I think 5 is out from mid digits for the same reason. 
# Not sure about 1 I think that's ok so we have possible mid digits of 1, 3, 7 and 9
# Still nothing obvious as to why there is a limit to the number of primes that can fit this pattern

# List out some primes to try and see why the pattern might be unachievable past a point
import sys
 
# setting path
sys.path.append('../Euler')
from common.helpers import SieveOfEratosthenes, is_prime

def is_truncatable_prime(prime):
    # Go left to right to see if it's a truncatable prime
    prime_str = str(prime)
    for i in range(1, len(prime_str)):
        if not is_prime(int(prime_str[i:])):
            return False
    # Go right to left to see if it's a truncatable prime
    for i in range(1, len(prime_str)):
        if not is_prime(int(prime_str[:-i])):
            return False
    return True

truncatable_primes = []
primes = SieveOfEratosthenes(1000000)
for prime in primes:
    if prime < 10:
        continue
    if is_truncatable_prime(prime):
        truncatable_primes.append(prime)
        print(f"{prime} is a truncatable prime")
    if len(truncatable_primes) == 11:
        break

print(sum(truncatable_primes))