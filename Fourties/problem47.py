# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from common.helpers import prime_factors

consecutive_count = 0
distinct_prime_count = 4

for i in range(1, 1000000):
    if len(prime_factors(i)) == distinct_prime_count:
        consecutive_count += 1
        if consecutive_count == distinct_prime_count:
            print(f"Found {distinct_prime_count} consecutive numbers with {distinct_prime_count} distinct prime factors starting with {i - distinct_prime_count + 1}")
            break
    else:
        consecutive_count = 0