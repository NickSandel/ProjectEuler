# The cube, 41063625(345**3), can be permuted to produce two other cubes: 56623104(384**3) and 
# 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

# Approach: generating random cubes and checking permutations seems like a bad idea but the most obvious brute force approach

# I think the key here is I know 345 ** 3 is the smallest which has exactly 3 (unless it's tricking me and there's a smaller one with 5 which is not exactly 3!!!)
# It's exact as well it's not an at least deal...
# I think generate cube numbers up to 1000 and then check for permutations from the set produced, stopping at 3 initially

from common.helpers import is_permutation

cubes = []
first_cube_length = 0
for n in range(4642, 12000):
    if first_cube_length == 0:
        first_cube_length = len(str(n**3))
    elif len(str(n**3)) > first_cube_length:
        print(f"Stopping at {n} as it's into a different lenth of number")
        break
    cubes.append(n**3)

permutations_sought = 5

for cube1 in cubes:
    permutations_found = 1
    for cube2 in cubes:
        if cube1 == cube2:
            continue
            # Do nothing
        elif is_permutation(cube1, cube2):
            permutations_found += 1

        if permutations_found == permutations_sought:
            print(f"Found lowest sought permutation: {cube1}")
            break
    if permutations_found == permutations_sought:
        break

# The above worked fine for finding the 3 but doesn't find any fives. It doesn't find any 4's either and I'd expect the permutations to get rarer as the digits increase
# Will expand the cubic range a bit first
# This worked to find the first 4 permutation, added in a clause so that only numbers with the same length of digits are included in the same set
# Then just slowly increased the range, hoping to keep it small and keep iterating to find the first 5 set
# Going in smallish sections of up to 5000 I haven't found any sets of 5 up to 20,000
# However it is dawning on me now I've inadvertently limited myself as I'm not getting the full range of digit length outputs!

# Haha not that elegant but I had missed it, 127035954683 is the correct answer!
# Brute force for the win!