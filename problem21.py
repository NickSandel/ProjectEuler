# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt, floor
def divisors_below_num(num):
    divisors = [1] # Don't add num itself
    # As seen with hunting for primes no point going lower than the square root as anything lower will have a pair number higher
    # so save the compute!
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(int(i))
            # Also add the opposite part
            divisors.append(int(num/i))
    return divisors

print(sum([int(x) for x in divisors_below_num(220)]))
print(sum([int(x) for x in divisors_below_num(284)]))

# So got a factorial function working nicely and adding them up how to iterate over the 10000 now?
# Brute force it to find the pairs?
# Hmm where to start the loop?
amicables = []
for i in range(4,10000 + 1):
    sum_fact = sum([int(x) for x in divisors_below_num(i)])
    if i != sum_fact and i == sum([int(x) for x in divisors_below_num(sum_fact)]):
        amicables.append(i)

print(amicables)
print(sum([int(x) for x in amicables]))