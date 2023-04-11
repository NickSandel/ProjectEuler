# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

# Lazy guess is to get primes up to 9 digits with the sieve then iterate through checking for pandigital ones?

# setting path
import sys
from common.helpers import SieveOfEratosthenes, is_prime

# primes = SieveOfEratosthenes(987654321)
# for prime in reversed(primes):
#     if is_pandigital(str(prime)):
#         print(f"Largest pandigital prime = {prime}")
#         break

# Hmm brute forcing this isn't working out well at all it's hanging on building the prime list - STOP
# Maybe the other way will be more optimal looking from pandigital numbers and seeing which are prime? Feels like I can get in a big tangle trying to do this again though...

# What rules can be enforced? It must end in 1,3,7 or 9 to be prime. If it ends in 9 it must be a 9 digit number to be pandigital
import itertools
from typing import List
def perm_iteration(digits: List[int], digit_append:int):
    permutations = itertools.permutations(digits)
    for perm in permutations:
        perm2 = perm + (digit_append,)
        if is_prime(int(''.join(map(str, perm2)))):
            print(int(''.join(map(str, perm2))))
            break

perm_iteration([9,8,6,5,4,3,2,1], 7)
perm_iteration([9,8,7,6,5,4,2,1], 3)
perm_iteration([9,8,7,6,5,4,3,2], 1)
# Ok so looks like none of the 9 digit ones are prime

perm_iteration([8,6,5,4,3,2,1], 7)
perm_iteration([8,7,6,5,4,2,1], 3)
perm_iteration([8,7,6,5,4,3,2], 1)
# 8 digits are no too

perm_iteration([7,6,5,4,2,1], 3)
# SOLVED!