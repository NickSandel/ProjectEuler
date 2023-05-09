# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from common.helpers import is_prime, SieveOfEratosthenes

# Get primes below 100
primes = sorted(SieveOfEratosthenes(50000))

# Some rules will help out here:
# After a point you will have reached the maximum possible consecutive count because the addition will take you over the limit
# E.g. after 100/2 any 2 additions will go over 100
# Going bottom up then makes the most sense to iterate?
# Having to skip a number for sequence breaks it

# I'm struggling to think how to go through this. 
# Do I go from a prime up until I hit the limit (1000) and find the largest length consec I can?

limit = 1000000
consecs_prime = 0
consec_starting_prime = 0
consec_ending_prime = 0
highest_total = 0
for i, prime in enumerate(primes):
    # Go to the limit checking for longest consec prime on the way
    rolling_value = prime
    for j in range(i+1, len(primes)):
        next_prime = primes[j]
        rolling_value += next_prime
        if rolling_value > limit:
            break
        if is_prime(rolling_value) and j-i > consecs_prime:
            consecs_prime = j-i+1
            consec_starting_prime = prime
            consec_ending_prime = next_prime
            highest_total = rolling_value

print(f"Longest consecutive sequence is of {consecs_prime} primes starting with {consec_starting_prime} and ending with {consec_ending_prime} with total {highest_total}")