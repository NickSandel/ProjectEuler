# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?



# I expect there is a way to do this in a clever way kind of feels like the factorial thing comes into play 
# here but not sure how to apply it
# Or do I set the max number of each coin based on £2 / coin and do some iteration off that to find combos?
# Some easy ones would be 2x£1 and 200x1p but harder would be 108x1p + 1x2p + 9x10p

# Hmm I wonder if I go from largest denomination down to smallest will I get all permutations by force iteration?
# E.g. loop from 2 down to 0 for £1 then 4 down to 0 for 50p etc and I should end up having covered all possible combos which hit £2? 
# In each sub loop start at the max available to get up to £2
from math import floor

coins = [200, 100, 50, 20, 10, 5, 2, 1]
desired_total = 200

def check_combo(counts):
    total = 0
    for index, counter in enumerate(counts):
        total += coins[index] * counter
    return total

combos = 0
for c0 in range(floor(desired_total/coins[0]), -1, -1):
    running_total = check_combo([c0])
    if running_total == desired_total:
        combos += 1
        continue
    for c1 in range(floor((desired_total-running_total)/coins[1]), -1, -1):
        running_total = check_combo([c0,c1])
        if running_total == desired_total:
            combos += 1
            continue
        for c2 in range(floor((desired_total-running_total)/coins[2]), -1, -1):
            running_total = check_combo([c0,c1,c2])
            if running_total == desired_total:
                combos += 1
                continue
            for c3 in range(floor((desired_total-running_total)/coins[3]), -1, -1):
                running_total = check_combo([c0,c1,c2,c3])
                if running_total == desired_total:
                    combos += 1
                    continue
                for c4 in range(floor((desired_total-running_total)/coins[4]), -1, -1):
                    running_total = check_combo([c0,c1,c2,c3,c4])
                    if running_total == desired_total:
                        combos += 1
                        continue
                    for c5 in range(floor((desired_total-running_total)/coins[5]), -1, -1):
                        running_total = check_combo([c0,c1,c2,c3,c4,c5])
                        if running_total == desired_total:
                            combos += 1
                            continue
                        for c6 in range(floor((desired_total-running_total)/coins[6]), -1, -1):
                            running_total = check_combo([c0,c1,c2,c3,c4,c5,c6])
                            if running_total == desired_total:
                                combos += 1
                                continue
                            for c7 in range(floor((desired_total-running_total)/coins[7]), -1, -1):
                                running_total = check_combo([c0,c1,c2,c3,c4,c5,c6,c7])
                                if running_total == desired_total:
                                    combos += 1
                                    continue
        
print(combos)
# Got 73681 which isn't right :( no idea why it isn't right!
# Copilot says 73682 so I'm close but not quite there why am I only 1 off!

# For desired total it says 11 combos so let's try and validate this:
# [100, 50, 20, 10, 5, 2, 1]
# 0x100
# 0x50
# 0x20
# 1x10
# 2x5
# 1x5 + 2x2 + 1x1
# 1x5 + 1x2 + 3x1
# 1x5 + 0x2 + 5x1
# 5x2
# 4x2 + 6x1
# 3x2 + 4x1
# 2x2 + 6x1
# 1x2 + 8x1
# 10x1
# == 11 combinations... ffs this doesn't help

# 20 says 41 combinations
# 1x20
# 2x10
# 1x10 + 2x5
# 1x10 + 1x5 + 2x2 + 1x1
# 1x10 + 1x5 + 1x2 + 3x1
# 1x10 + 1x5 + 5x1
# 1x10 + 5x2
# 1x10 + 4x2 + 2x1
# 1x10 + 3x2 + 4x1
# 1x10 + 2x2 + 6x1
# 1x10 + 1x2 + 8x1
# 1x10 + 10x1
# 4x5
# 3x5 + 2x2 + 1x1
# 3x5 + 1x2 + 3x1
# 3x5 + 5x1
# 2x5 + 5x2
# 2x5 + 4x2 + 2x1
# 2x5 + 3x2 + 4x1
# 2x5 + 2x2 + 6x1
# 2x5 + 1x2 + 8x1
# 2x5 + 10x1
# 1x5 + 7x2 + 1x1
# 1x5 + 6x2 + 3x1
# 1x5 + 5x2 + 5x1
# 1x5 + 4x2 + 7x1
# 1x5 + 3x2 + 9x1
# 1x5 + 2x2 + 11x1
# 1x5 + 1x2 + 13x1
# 1x5 + 15x1
# 10x2
# 9x2 + 2x1
# 8x2 + 4x1
# 7x2 + 6x1
# 6x2 + 8x1
# 5x2 + 10x1
# 4x2 + 12x1
# 3x2 + 14x1
# 2x2 + 16x1
# 1x2 + 18x1
# 20x1
# == 41 is correct!!! Argh no hint as to why I got this wrong :(