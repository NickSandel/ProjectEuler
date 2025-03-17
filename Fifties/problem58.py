# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 
# 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 
# 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9
# will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes 
# along both diagonals first falls below 10% ?

from common.helpers import is_prime

# I think the trick here is that I don't need to generate all of the numbers at all
# I think surely I can just generate the corner numbers? Then I can just query how many are primes to get the ratio

# Test in a small way first
# Length square n will have 4 values (outside of n = 1) and they will have values x + n-1, x + 2n -1, x + 3n-1, x + 4n-1 where x is the last number from the prior spiral

square1 = [1]
square3 = [1,
           3,5,7,9] # Diff between layers = 2
square5 = [1,
           3,5,7,9, # Diff between layers = 2
           13,17,21,25] # Diff between layers = 4
square7 = [1,
           3,5,7,9, # Diff between layers = 2
           13,17,21,25, # Diff between layers = 4
           31,37,43,49] # Diff between layers = 6

# So the next layer will be 49 + 8 then 8 diff
square9 = [1,
           3,5,7,9, # Diff between layers = 2
           13,17,21,25, # Diff between layers = 4
           31,37,43,49, # Diff between layers = 6
           57,65,73,81] # Diff between layers = 8

# Ok so formula for a new layer is length l + 2, new numbers are l-1 different from one another

# Maybe there is a smarter way than brute force but I'm going to use this to try it

def add_new_spiral_corners(length, prime_count):
    # new_corners = []
    latest_corner = (length - 2) ** 2
    for i in range(1, 4):
        latest_corner += length - 1
        if is_prime(latest_corner):
            prime_count += 1
        # new_corners.append(latest_corner)
    return prime_count

# test_corners = [1]
# test_corner = 1
# for i in range(1, 7, 2):
#     test_corners, test_corner = add_new_spiral_corners(i, test_corners, test_corner)
#     print(test_corners)

# def generate_sprial_numbers(length):
#     current_number = 1
#     sprial_corners = [current_number]
#     for i in range(1, int((length + 1) / 2)): # Layers to iterate through
#         for ii in range(1, 5):
#             current_number += i * 2
#             sprial_corners.append(current_number)
#     return sprial_corners

# def test_prime_ratio(numbers):
#     prime_count = 0
#     for i in range(len(numbers)):
#         if is_prime(numbers[i]):
#             prime_count += 1
    
#     return prime_count / len(numbers)

# print(generate_sprial_numbers(1))
# print(generate_sprial_numbers(3))
# print(generate_sprial_numbers(5))

# test = generate_sprial_numbers(7)
# print(test)
# print(test_prime_ratio(test))

# I wonder if the last number is always guaranteed to be non-prime as well...
# Last corner number is always n**2 where n = length

# test_corners = [1]
# latest_diagonal = []
# total_diagonals = 1
# test_corner = 1
prime_count = 0
for length in range(3, 1000000, 2):
    prime_count = add_new_spiral_corners(length, prime_count)
    total_diagonals += 4
    ratio = prime_count / total_diagonals
    if ratio < 0.1:
        print(ratio)
        print(length)
        break

# This is more efficient than my first approach but still very inefficient!
# Needs a rethink, I'm sure it shouldn't take very long to run
# I don't need to keep each new spiral just check how many primes are in it and increment 
# a counter for how many other numbers there would be and in this I can ignore the
# 4th corner as it'll always be length ** 2

# Eventually optimised this enough by ignoring the array and just adding up new primes and the total diagnoal size
# and fixed some flaws in how it was working