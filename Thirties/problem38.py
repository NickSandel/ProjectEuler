# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# As is good practice start with something which solves the above
def is_pandigital(number: str):
    digits = sorted(number)
    for i, d in enumerate(digits):
        if d != str(i + 1):
            return False
    return True

def concat_multiples(multiplicand: int, multipliers):
    results = ""
    for multiplier in multipliers:
        results += str(multiplicand * multiplier)
    return results

# concat_prod = concat_multiples(192, [1,2,3])
# print(concat_prod)
# if is_pandigital(concat_prod):
#     print("True")

# concat_prod2 = concat_multiples(9, [1,2,3,4,5])
# print(concat_prod2)
# if is_pandigital(concat_prod2):
#     print("True")

# Ha I thought it might be a trick as it's asking for the largest which can be formed like this I thought we can't have a value larger than beginning with 9 
# so I tried 918273645 but it's wrong

# I think the first digit has to be 9 the ultimate one would be 987654321 but as n has to be > 1 it can't be 987654321 with [1]
# The problem seems to be one of search but I'm quite sure the first in array needing to be 1 means the first digit in the number must be 9 
# as nothing * 1 can make a 9 starter and we already have the benchmark from the example showing it must be greater than 918273645

# I think the examples also elude to a cap I don't think the array can be larger than 1-5 else it would produce higher numbers 
# so maybe I need to search in 2 digits starting with 9 and arrays 1-4?

for d2 in range(0,9):
    concat_prod = concat_multiples(90 + d2, [1,2,3])
    if is_pandigital(concat_prod):
        print(f"{90 + d2} * [1,2,3] makes the pandigital value: {concat_prod}")

# Finds nothing try higher
for d3 in range(0,999):
    concat_prod = concat_multiples(9000 + d3, [1,2])
    if is_pandigital(concat_prod):
        print(f"{90 + d2} * [1,2] makes the pandigital value: {concat_prod}")

# Bam answer is 932718654