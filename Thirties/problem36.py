# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

import sys
 
# setting path
from common.helpers import is_palindrome

bit_pals = []
for i in range(1, 1000000):
    if is_palindrome(i):
        bit_version = int(f"{i:b}")
        if is_palindrome(bit_version):
            bit_pals.append(i)

print(sum(bit_pals))
