# It is possible to write five as a sum in exactly six different ways:
        # 4+1
        # 3+2
        # 3+1+1
        # 2+2+1
        # 2+1+1+1
        # 1+1+1+1+1

# How many different ways can one hundred be written as a sum of at least two positive integers?

# Manual step how many sums up to 6 can there be? Start with the five batch and add 1 to each line
        # 4+1+1
        # 3+2+1
        # 3+1+1+1
        # 2+2+1+1
        # 2+1+1+1+1
        # 1+1+1+1+1+1

# How many new combinations now?

# All together:
        # 5+1
        # 4+2
        # 4+1+1
        # 3+3
        # 3+2+1
        # 3+1+1+1
        # 2+2+2
        # 2+2+1+1
        # 2+1+1+1+1
        # 1+1+1+1+1+1
# = 10 permutations
# So what's the process and sticking points?
# Maybe it's something like n-1 will have 1 permutation, n-2 will have 2 permutations, n-3 will have 3? Doubt it that seems too simple
# I think the sticking point is really just about how many combos for n-x see in the 6 decomposition 3 and 2 have an extra row of data maybe that's because they're factors of 6?

# What does 7 look like?

# All together:
    # 6+1
    # 5+2
    # 5+1+1
    # 4+3
    # 4+2+1
    # 4+1+1+1
    # 3+3+1
    # 3+2+2
    # 3+2+1+1
    # 3+1+1+1+1
    # 2+2+2+1
    # 2+2+1+1+1
    # 2+1+1+1+1+1
    # 1+1+1+1+1+1+1

# = 14 permutations

# I think something special is happening around n/2 as that's the point where permutation counts drop a lot compared to lower down

# Manually do an even bigger one 20

# 19+1
1
# 18+2
# 18+1+1
2
# 17+3
# 17+2+1
# 17+1+1+1
3
# 16+4
# 16+3+1
# 16+2+2
# 16+2+1+1
# 16+1+1+1+1
4
# 15+5
# 15+4+1
# 15+3+2
# 15+3+1+1
# 15+2+1+1+1
# 15+1+1+1+1+1
5
# 14+6
# 14+5+1
# 14+4+2
# 14+4+1+1
# 14+3+3
# 14+3+2+1
# 14+3+1+1+1
# 14+2+2+2
# 14+2+2+1+1
# 14+2+1+1+1+1
# 14+1+1+1+1+1+1
11
# 13+7
# 13+6+1
# 13+5+2
# 13+5+1+1
# 13+4+3
# 13+4+2+1
# 13+4+1+1+1
# 13+3+3+1
# 13+3+2+1+1
# 13+3+1+1+1+1
# 13+2+2+2+1
# 13+2+2+1+1+1
# 13+2+1+1+1+1+1
# 13+1+1+1+1+1+1+1
14
# 12+8
# 12+7+1
# 12+6+2
# 12+6+1+1
# 12+5+3
# 12+5+2+1
# 12+5+1+1+1
# 12+4+4
# 12+4+3+1
# 12+4+2+1+1
# 12+4+1+1+1+1
# 12+3+3+2
# 12+3+3+1+1
# 12+3+2+2+1
# 12+3+2+1+1+1
# 12+3+1+1+1+1+1
# 12+2+2+2+2
# 12+2+2+2+1+1
# 12+2+2+1+1+1+1
# 12+2+1+1+1+1+1+1
# 12+1+1+1+1+1+1+1+1
21
# 11+9
# 11+8+1
# 11+7+2
# 11+7+1+1
# 11+6+3
# 11+6+2+1
# 11+6+1+1+1
# 11+5+4
# 11+5+3+1
# 11+5+2+1+1
# 11+5+1+1+1+1
# 11+4+4+1
# 11+4+3+2
# 11+4+3+1+1
# 11+4+2+2+1
# 11+4+2+1+1+1
# 11+4+1+1+1+1+1
# 11+3+3+3
# 11+3+3+2+1
# 11+3+3+1+1+1
# 11+3+2+2+2
# 11+3+2+2+1+1
# 11+3+2+1+1+1+1
# 11+3+1+1+1+1+1+1
# 11+2+2+2+2+1
# 11+2+2+2+1+1+1
# 11+2+2+1+1+1+1+1
# 11+2+1+1+1+1+1+1+1
# 11+1+1+1+1+1+1+1+1+1
28

# One intersting rule is that the next number added must be equal or less than the current number 
# as once we tip past 10 then we can't have 9+11 as it's already accounted for in the 11 section

# Potential algorithm for listing them appears to be say x is the current number being based from then combinations from x start with x+x if possible else x+x-1
# Then we do x + x-2 etc until x-y = 1 when we stop and that's the last set
# But for y being x-iteration we have to find all combinations starting with Cy where C=total-x/y
# E.g. total=20 for x=14 we start with total-x=6 as the iteration counter then walk that down
# On each iteration counter the first value will be total-iteration

import functools
from math import floor

def combo_generator(number):
    combos = []
    iteration = 0
    halfway = number / 2
    x = number - 1
    while x > 0:
        y = number - x
        # for i in range(number-x):
            # while y <= x:
            #     combo = [x,y]
            #     for ii in range(1, int(floor((number-x)/y))):
            #         combo.append(ii)
            #         combos.append(combo)
            #     y += 1


        # if y > x:
        #     break
        combo = [x,y]
        for ii in range(0, int(floor((number-x)/y))):
            for i in range(y):
                combos.append(combo)
            # combos.append([x,y])
            # y -= 1
        x -= 1
    return combos


# I gave up on my own and searched for a solution which I found at
# https://martin-ueding.de/posts/project-euler-solution-76-counting-summations/
# Key thing was not to just take this but understand what it's doing
# I had achieved the key insight that you have to walk down the tree so once you've hit say 3+2 you can't have 2+3 as it would be a duplicate
# The section min(number - x, x) is also directly doing the part I was trying and failing to do where in for say 20=14+6 it recognises that can be 14+2*3 
# which itself means each 2 can be broken down into a new combination
@functools.cache
def partitions(number: int, top: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        result = sum(
            partitions(number - x, min(number - x, x)) for x in range(1, top + 1)
        )
        if number <= top:
            result += 1
        return result
    
def num_partitions(number: int) -> int:
    return partitions(number, number)

print (num_partitions(5) - 1)
print (num_partitions(6) - 1)
print (num_partitions(7) - 1)
print (num_partitions(100) - 1)

# I ran out of time to try and do this another way and I'm pretty sure it would have been clunky and slow, I'll use the answer I found