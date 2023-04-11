# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# Ha just used my prime_lister.py. Set n to 200,000 and let it churn away it found 17984 primes so went a bit overkill but did then pull out the one I wanted. Code copied here for completeness:
import sys
 
# setting path
import numbers
from common.helpers import is_prime
oddNumbers = [1,3,5,7,9]
evenNumbers = [0,2,4,6,8]

numberRange = 200000
divisorList = []
primes = []

for i in range (numberRange):
    if is_prime(i):
        primes.append(i)
    if len(primes) == 10002:
        break
		
print(len(primes))
print(sorted(primes))
print(sorted(primes)[10001])