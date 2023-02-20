# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

# Seems simplest to get all primes below a million then iterate through to find the circular ones 
# When iterating to check if circular only need to go through digits of same length which might give a nice shortcut

# Gather all primes below 100 to start with to build logic against the above known list
import sys
 
# setting path
sys.path.append('../Euler')
from common.helpers import SieveOfEratosthenes, is_prime

primes = SieveOfEratosthenes(1000000)

# I was tricked! This isn't about permutations which was my first approach, it's about ROTATIONS!
def get_rotations(num):
    rotations = []
    num = str(num)
    for i in range(len(num)):
        rotations.append(int(num[i:] + num[:i]))
    return rotations

circular_primes = []
# Go through each set of primes by number of digits
for prime in primes:
    # If primes < 10 it's circular by definition
    if prime < 10:
        circular_primes.append(prime)
    else:
        # Get all rotations of digits
        rotations = list(get_rotations(prime))
        # Check if all rotations are in the primes set
        for rotation in rotations:
            if not is_prime(rotation):
                break
        else:
            circular_primes.append(prime)

print(circular_primes)
print(len(circular_primes))