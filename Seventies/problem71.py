from math import gcd

# Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d) = 1,
# it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
# 1/8
# 1/7
# 1/6
# 1/5
# 1/4
# 2/7
# 1/3
# 3/8
# 2/5
# 3/7
# 1/2
# 4/7
# 3/5
# 5/8
# 2/3
# 5/7
# 3/4
# 4/5
# 5/6
# 6/7
# 7/8

# It can be seen that 2/5 is the fraction immediately to the left of 3/7.

# By listing the set of reduced proper fractions for d <= 1,000,000 in ascending
# order of size, find the numerator of the fraction immediately to the left of 3/7.

# Ok so playing around a little there's some pattern to how the numbers go
# 1/8 goes to 1/4 before we see 2/7
# 1/1,000,000 goes to 1/500,000 before we see 2/999,999

# One great starting point for this is (1,000,000 / 7 ) * 3 = 428571 as 428571/1,000,000 = 0.428571
#  and 3/7 = 0.42857142857142855
# I must remember the HCF = 1 element I have no idea if 428571/1,000,000 is a reduced proper fraction

# So the first function I need is to make a reduced proper fraction?
# Maybe but I also think there will be other fractions between 428571/1,000,000 and 3/7 I just think this
# one is a good starting point to go up from
# I think it's more about skipping over the fractions which can reduce down

from common.helpers import is_prime, prime_factors

n_test = 428571
divisor = gcd(n_test, 1000000)

print(n_test / divisor)


print(428572 / 1000000)
print(1 / 428571)

n_test = 428571
divisor = gcd(n_test, 999999)
# Ah this 428571/999999 == 3/7

print(n_test / divisor)


n_test = 428570
divisor = gcd(n_test, 999999)
# Ah this 428571/999999 == 3/7

print(n_test / divisor)
# Haha! Screw compute I just did this one manually!

# Method to my madness:
# - Find how 3/7 translates to x/1,000,000 and find x rounded down
# - Compare the decimal values of 3/7 to x/1,000,000
# - Recognise that the next big step before that is x-1/1,000,000 but it's likely a sub-step in between
# - Recognise that x-1/1,000,000 - 1 is the next sub step and slowly decrease the divisor
# - Check the fractions and tried to submit 428570 which is rounded x-1 so almost too easy!
