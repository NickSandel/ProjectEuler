# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, 
# and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

# Brute force seems ok here as there won't be that many. Step one is to use the sieve to get all primes between 1000 and 9999
from common.helpers import SieveOfEratosthenes, is_permutation

def in_range(item):
    return item > 999 and item < 10000

primes = SieveOfEratosthenes(9999)
primes = set(filter(in_range, primes))

# Got the primes now what? Group by permutations? My guess is there aren't many sets with 3 or more permutations

perms = []
while primes:
    prime = primes.pop()
    matches = []
    for prime_perm in primes:
        if is_permutation(prime_perm, prime):
            matches.append(prime_perm)
    for prime_perm in matches:
        primes.remove(prime_perm)
    matches.append(prime)
    perms.append(matches)

def has_three_equidistant(perm_list):
    # To find if we have 3 equidistant terms need to go through the whole list and see if we can find the triplet
    for i in range(len(perm_list)):
        for j in range(i+1, len(perm_list)):
            for k in range(j+1, len(perm_list)):
                if perm_list[j] - perm_list[i] == perm_list[k] - perm_list[j]:
                    return True, perm_list[i], perm_list[j], perm_list[k]
    return False, None, None, None

for perm_list in perms:
    if len(perm_list) >= 3:
        perm_list = sorted(perm_list)
        has_three, first, second, third = has_three_equidistant(perm_list)
        if has_three:
            print(f"{first}{second}{third}")