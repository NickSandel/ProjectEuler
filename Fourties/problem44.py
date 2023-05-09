# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

def pentagonal_number_generator():
    n = 1
    while True:
        next_pentagonal = n*(3*n - 1)/2
        yield(next_pentagonal)
        n += 1

# # List first 10 pentagonals
# pentagonals = []
# for pentagonal in pentagonal_number_generator():
#     pentagonals.append(pentagonal)
#     if len(pentagonals) == 20:
#         break

# print(pentagonals)

# # Show how the numbers grow
# for i in range(1,len(pentagonals)):
#     print(pentagonals[i] - pentagonals[i-1])

# The difference is growing by 3 each time and it is just growing as expected
# so basically the first pair I can find which satisfy the condition will produce the lowest D
# The tricky part seems to be how to assess both conditions?

# So if p2-p1 = 1 + 3(2-1) is the difference always px-pn = x-n + 3(x-n)?
# p3 = 12, p1 = 1 = 1 + 3(3-1) = 7 WRONG how about 1 + 3(x-n*x-n) = 1 + 3(2*2) = 13 it's really 1 + 3(3-1) + 1 + 3(2-1) but how do I condense that?
# 1 + 3(3-1) + 1 + 3(2-1) == 2 + 3(2) + 3(1) == 2 + 3(3) == x-n + 3(x-n+1)
# p5 = 35, p3 = 12, D = 5-3 + 3(5-3+1) == 2 + 3(3) == 11 WRONG diff is 23 what it should be is 1 + 3(5-1) + 1 + 3(3-1) == 2 + 3(7)
# What the difference really does is the sum of all the sequence to the x minus the sequence before n is it more like this:
# p5 = 5 + 3(4) + 3(3) + 3(2) + 3(1) == 35 - p2 = 2 + 3(2) + 3(1) == 11 35-11-1(first in sequence?) == 24
# Condense them? px = x + 3(x-1) + 3(x-2)
# From wikipedia it says: The nth pentagonal number is the sum of n integers starting from n (i.e. from n to 2n-1). The following relationships also hold:
# pn = pn-1 + 3n-2 = 2pn-1 - pn-2 + 3

# Go through each previous pairing of pentagonals and see if their sum meets the new value 
# and if their difference equals a different pentagonal value
# for i, p1 in enumerate(pentagonals):
#     for i2 in range(i + 1, len(pentagonals)):
#         sum_pents = p1 + pentagonals[i2]
#         diff_pents = pentagonals[i2] - p1
#         if sum_pents in pentagonals and diff_pents in pentagonals:
#             print(f"Found THE pairing with p{i} = {p1} and p{i2} = {pentagonals[i2]} with a diff of {diff_pents}")
#             break
#         # if sum_pents in pentagonals:
#         #     print(f"Found a pairing with p{i} = {p1} and p{i2} = {pentagonals[i2]} with a sum of {sum_pents}")
#         if diff_pents in pentagonals:
#             print(f"Found a pairing with p{i} = {p1} and p{i2} = {pentagonals[i2]} with a diff of {diff_pents}")

# Brute force isn't working like this it's just too dam slow. I'm clearly missing something important though like there's 
# no point comparing a bunch of items which don't add up to a new item and as the gap keeps growing there's something in not bothering to compare ones which clearly can't add up

# Observing the indices of p1 and p2 on the flagged sum and diff doesn't seem to give me any decent limits to iterate within, 
# I was hoping to see a pattern like "the diff indices never reach more than 10 apart" but alas tis not there

from math import sqrt

# Function to return True if a number is pentagonal
def is_pentagonal(n: int):
    # A number is pentagonal if it can be calculated with the formula: Pn=n(3n−1)/2
    # So we can solve for n and see if it's an integer
    n = (1 + sqrt(1 + 24*n))/6
    return n.is_integer()


pentagonals = []
for pentagonal in pentagonal_number_generator():
    pentagonals.append(pentagonal)
    if len(pentagonals) == 3000:
        break

for i, p1 in enumerate(pentagonals):
    for i2 in range(i + 1, len(pentagonals)):
        if is_pentagonal(pentagonals[i2] - p1) and is_pentagonal(p1 + pentagonals[i2]):
            print(f"Found the pairing with p{i} = {p1} and p{i2} = {pentagonals[i2]} with a diff of {pentagonals[i2] - p1}")
            break