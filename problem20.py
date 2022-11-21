# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# Is 100! too large to be a proper number?
factorial = 1
for i in range(1,101):
    factorial = factorial * i

print(factorial)


sum_factorial = [int(x) for x in str(factorial)]
print(sum(sum_factorial))
# 100! = 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000

# From the forum someone posted this:
from functools import reduce
print(reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))]))