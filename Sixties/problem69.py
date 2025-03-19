# Euler's totient function, O|(n) [sometimes called the phi function], is defined as the number of positive integers 
# not exceeding n which are relatively prime to n. For example, as 1,2,4,5,7 and 8 are all less than or equal to nine 
# and relatively prime to nine, O|(9) = 6.

# n | Relatively Prime | O|(n) | n/O|(n)
# 2	| 1	               | 1	   | 2
# 3	| 1,2	           | 2	   | 1.5
# 4	| 1,3	           | 2	   | 2
# 5	| 1,2,3,4	       | 4	   | 1.25
# 6	| 1,5	           | 2	   | 3
# 7	| 1,2,3,4,5,6	   | 6	   | 1.1666...
# 8	| 1,3,5,7	       | 4	   | 2
# 9	| 1,2,4,5,7,8	   | 6	   | 1.5
# 10| 1,3,7,9	       | 4	   | 2.5
# It can be seen that n = 6 produces a maximum n/O|(n) for n <= 10.

# Find the value of n <= 1,000,000 for which n/O|(n) is a maximum.

# I don't think brute force is a good idea here
# Notes from this brief sample:
# Primes are the worst so I think the answer will be a composite number
# What this really wants is the most composite number possible so the primes which can't 
# contribute to it are minimised
# I wonder if flipping as a problem is better something like getting the primes below 500,000 (half of a million)
# And then finding the largest composite number which covers the most primes?
# Is it true then that if a number can divide by it's prime then it can divide by composites made of that prime up to a point?
# What point should that be?
# Take 18 that can divide by 9, 6, 3, 1. 3 prime composites up to 6 and 9
# 28 divides by 14, 7, 4, 2, 1

# Ah misunderstoon what relatively prime means, I wonder if it is back to square root and find the largest composite number
# which contains the most primes below this square root value?

# So maybe an approach of find the highest prime < 1000, square it and work back through lower primes to see how many divide by the end value?

from common.helpers import is_prime, SieveOfEratosthenes
primes_1000 = SieveOfEratosthenes(1000)

print(primes_1000)
primes_1000 = sorted(list(primes_1000))

def totient(n, prime_factors):
    totient = n
    for p in prime_factors:
        totient = totient * (1-1/p)
    return totient

# print(totient(6, [2,3])) # Expecting 2
# print(totient(8, [2])) # Expecting 4
# print(totient(20, [2,5])) # Expecting 8

# 509 is the largest
largest_prime_factors = []
largest_prime_square = 0
totient_ratio_max = 0
for n in range(1000000, 1, -1):
    n_primes = []
    #nn = primes_1000[n] ** 2
    #nn = n ** 2
    nn = n
    # prime_factors = 1 # 1 is always one
    for p in primes_1000:
        if nn % p == 0:
            # prime_factors += 1
            n_primes.append(p)
    totient_ratio = nn/totient(n, n_primes)
    if totient_ratio > totient_ratio_max:
        largest_prime_factors = n_primes
        largest_prime_square = nn
        totient_ratio_max = totient_ratio

print(largest_prime_factors)
print(largest_prime_square)
print(totient_ratio_max)

# First approach was to find the number with the maximum amount of primes
# 8
# 930930
# Also incorrect!

# https://en.m.wikipedia.org/w/index.php?title=Euler%27s_totient_function&wprov=rarw1 has some interesting content
# I think I might be on the right tracks here but I missed a key step. Once I have the primes I can calculate the value of phi
# to calculate I need to do n times (for each prime (1-1/prime)) to get the value

# [2, 3, 5, 7, 11, 13, 17]
# 510510
# 5.539388020833331
# Answer = 510510
# It ran a bit slowly, quite sure there's an optimisation somewhere maybe around monitoring the ratio and stopping early but it didn't take too long
# I suspect the first approach was missing the key value of those primes not being numerous but being the smallest size so that they yield the highest output n