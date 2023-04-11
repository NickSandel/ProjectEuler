# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
# but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

l = list(permutations(['0','1','2','3','4','5','6','7','8','9']))

# Remove any numbers that start with 0
l = [x for x in l if x[0] != 0]

# Remove any where digits 2-4 are not divisible by 2
l = [x for x in l if int(''.join(x[1:4])) % 2 == 0]

# Remove any where digits 3-5 are not divisible by 3
l = [x for x in l if int(''.join(x[2:5])) % 3 == 0]

# Remove any where digits 4-6 are not divisible by 5
l = [x for x in l if int(''.join(x[3:6])) % 5 == 0]

# Remove any where digits 5-7 are not divisible by 7
l = [x for x in l if int(''.join(x[4:7])) % 7 == 0]

# Remove any where digits 6-8 are not divisible by 11
l = [x for x in l if int(''.join(x[5:8])) % 11 == 0]

# Remove any where digits 7-9 are not divisible by 13
l = [x for x in l if int(''.join(x[6:9])) % 13 == 0]

# Remove any where digits 8-10 are not divisible by 17
l = [x for x in l if int(''.join(x[7:10])) % 17 == 0]

# Print sum of all numbers left
print(sum([int(''.join(x)) for x in l]))