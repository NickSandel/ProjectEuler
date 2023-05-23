# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 
# (5 | 3) = 10

# In general, (n | r) = ( n! | r!(n−r)! ) , where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.


# It is not until n = 23, that a value exceeds one-million: 
# ( 23 | 10 ) = 1144066.

# How many, not necessarily distinct, values of (n | r) for 1 ≤ n ≤ 100, are greater than one-million?

import math
# Ok so one quick base truth: 9! is 362880 so nothing below n = 10 is worth testing for.

counter = 0
for n in range(23, 101):
    for r in range(n-1, 0, -1):
        if (math.factorial(n)/ (math.factorial(r) * math.factorial(n-r))) > 1000000:
            counter += 1
            # print(f"Found one over a million for n = {n} and r = {r}")

print(counter)