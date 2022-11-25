# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as 
# the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# ------------------------------------------------------------------------------------------
# \ | /
#  \|/
#  /|\
# / | \
# | | |
# | | |
#   |
# Decoding the question first... I think it means 28123 is the upper limit to bother with so fine. 
# Need to either find all values below this which are abundant... then pause and think more about how to find numbers which can't be expressed as the sum of 2 abundants...
# Unless this is sneaky! Does this mean that if a number is perfect or deficient then it cannot be expressed as the sum of 2 abundants? I think it might mean this
from math import sqrt, floor

def get_divisors(number):
    divisors = [1] # Don't add num itself
    # As seen with hunting for primes no point going lower than the square root as anything lower will have a pair number higher
    # so save the compute!
    for i in range(2, floor(sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(int(i))
            # Also add the opposite part (so long as it doesn't equal the number itself!)
            if int(number/i) != int(i):
                divisors.append(int(number/i))
    return divisors

def is_abundant(number):
    divisors = get_divisors(number)
    if sum(divisors) > number:
        return True
    else:
        return False

# # So I reckon if I just add up all the numbers which aren't abundant below 28123 then this gives me the answer I want...
# sum_non_abundant = 0
# for i in range(1, 28123 + 1):
#     # This will not add in 12-23 which are abundant numbers so need to just add them regardless (as the question asks about sum of abundants)
#     if i < 24:
#         sum_non_abundant += i
#     else:
#         sum_non_abundant += i if not is_abundant(i) else 0

# # ProjectEuler did not like this answer...
# # Nor my attempts to correct with a few mistakes I'd made
# print(sum_non_abundant)

# for i in range(1,40):
#     divisors = get_divisors(i)
#     print(i)
#     print(divisors)
#     if sum(divisors) == i:
#         print('perfect')
#     elif sum(divisors) < i:
#         print('deficient')
#     else:
#         print('abundant')

# This shows my logic to be false because the 2 of the lowest abundant numbers are 12 and 20 which add to 32 which is itself not an abundant number
# Maybe it needs more computation is all - get all abundant numbers below 28123 then iterate all other numbers in the space and check if they can be summed from abundant numbers only...

# How many abundant numbers are there below this threshold?
abundants_even = []
abundants_odd = []
for i in range(1, 28123 + 1):
    # This will not add in 12-23 which are abundant numbers so need to just add them regardless (as the question asks about sum of abundants)
    if is_abundant(i):# and i % 2 != 0: # There are odd ones but really not many!
        if i % 2 == 0:
            abundants_even.append(i)
        else:
            abundants_odd.append(i)


# 945 is the smallest odd abundant number so all odd numbers less than 945 + 12 = 957 are included in the sum I want

# Maybe it needs more computation is all - get all abundant numbers below 28123 then iterate all other numbers in the space and check if they can be summed from abundant numbers only...
# sum_non_abundant = 0
# for i in range(1, 28123 + 1):
#     # Loop through all numbers smaller than i - 12 in the abundandts list to see if there is a pair
#     can_pair = False       
#     for a in abundants:
#         if a > i - 12:
#             break
#         else:
#             if (i - a) in abundants:
#                 # print(f"i: {i} can be made of a:{a} and {i-a}")
#                 can_pair = True
#                 break
    
#     if can_pair is False:
#         sum_non_abundant += i

# print(sum_non_abundant)
# This is shit there clearly must be a better way than iterating the fuck out of this problem... not sure I see how though

# 46 looks to be the lowest even number which cannot be an addition of abundants maybe this is a clue. 
# I can brute force these low numbers then above maybe it's all about using the smaller set of odd numbers to see if they pair with an even one

sum_non_abundant = 0
for i in range(1, 28123 + 1):
    can_pair = False
    if i < 47:
        # Check if it CAN'T be made from the smaller even abundants
        for a in abundants_even:
            if a > i - 12:
                break
            else:
                if (i - a) in abundants_even:
                    # print(f"i: {i} can be made of a:{a} and {i-a}")
                    can_pair = True
                    break
    # After 46 there is no point looking at evens, they can all pair (tested up to 1000 anyway!)
    elif i % 2 == 0:
        can_pair = True
    else:
        # Loop through all numbers smaller than i - 12 in the abundandts list to see if there is a pair
        can_pair = False       
        for a in abundants_odd:
            if a > i - 12:
                break
            else:
                if (i - a) in abundants_even:
                    # print(f"i: {i} can be made of a:{a} and {i-a}")
                    can_pair = True
                    break
    
    if can_pair is False:
        sum_non_abundant += i

print(sum_non_abundant)