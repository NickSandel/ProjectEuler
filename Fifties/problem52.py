# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from common.helpers import is_permutation

if is_permutation(125874, 251748):
    print("True")

for i in range(1, 999999):
    if is_permutation(i, 2*i) and is_permutation(i, 3*i) and is_permutation(i, 4*i) and is_permutation(i, 5*i) and is_permutation(i, 6*i):
        print(i)
        break