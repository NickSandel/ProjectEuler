# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import sys
 
# setting path
sys.path.append('../Euler')
from common.helpers import is_prime

# Start with the 5 digit numbers
# Patterns for 3 fixed digits and 2 repeating:
# [1-9][0-9][*][*][1,3,7,9]
# [1-9][*][0-9][*][1,3,7,9]
# [1-9][*][*][0-9][1,3,7,9]
# [*][0-9][*][0-9][1,3,7,9]
# [*][*][0-9][0-9][1,3,7,9]
# How many combos where last digit is fixed and at least 2 others have to be fixed? But the rest can be 0-9
# largest_group = []
# for last_digit in [1,3,7,9]:
#     # Fix the first 2 digits
#     for first_digit in range(1,10):
#         for second_digit in range(0,10):
#             group_1 = []
#             group_2 = []
#             group_3 = []
#             # Now fix the last 2 digits
#             for repeated_digit in range(0,10):
#                 number = int(f"{first_digit}{second_digit}{repeated_digit}{repeated_digit}{last_digit}")
#                 if is_prime(number):
#                     group_1.append(number)
#                 number = int(f"{first_digit}{repeated_digit}{repeated_digit}{second_digit}{last_digit}")
#                 if is_prime(number):
#                     group_2.append(number)
#                 number = int(f"{first_digit}{repeated_digit}{second_digit}{repeated_digit}{last_digit}")
#                 if is_prime(number):
#                     group_3.append(number)

#             if len(group_1) > len(largest_group):
#                 largest_group = group_1
#             if len(group_2) > len(largest_group):
#                 largest_group = group_2
#             if len(group_3) > len(largest_group):
#                 largest_group = group_3

# print(largest_group)
# # Fuck me this worked!

# How do I code it up to be dynamic?
# How do I set the combination sequence in the first place? 4!(digits to vary)/(2! (stars)/2! (numbers)) = 6
# Patterns for 3 fixed digits and 2 repeating:
# [1-9][0-9][*][*][1,3,7,9]
# [1-9][*][0-9][*][1,3,7,9]
# [1-9][*][*][0-9][1,3,7,9]
# [*][*][0-9][0-9][1,3,7,9]
# [*][0-9][0-9][*][1,3,7,9]
# [*][0-9][*][0-9][1,3,7,9]

# How many for 4 digits? 3!(digits to vary)/2! (stars)/1! (numbers) = 3
# [0-9][*][*]
# [*][0-9][*]
# [*][*][0-9]

# How many for 4 digits? 5!(digits to vary)/3! (stars)/2! (numbers) = 10

# Patterns for 3 fixed digits and 3 repeating:
# [1-9][0-9][0-9][*][*][1,3,7,9]
# [1-9][0-9][*][0-9][*][1,3,7,9]
# [1-9][*][0-9][0-9][*][1,3,7,9]
# [1-9][*][0-9][*][0-9][1,3,7,9]
# [1-9][*][*][0-9][0-9][1,3,7,9]
# [1-9][0-9][*][*][0-9][1,3,7,9]

# [*][0-9][0-9][0-9][*][1,3,7,9]
# [*][0-9][0-9][*][0-9][1,3,7,9]
# [*][0-9][*][0-9][0-9][1,3,7,9]
# [*][*][0-9][0-9][0-9][1,3,7,9]

class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1


# # Now let's try with a 6 digit number
# # How many combos where last digit is fixed and at least 2 others have to be fixed? But the rest can be 0-9
# a = list(perm_unique(["*","*","*","N1","N2"]))

### This is how it was actually solved ###
# # This is the mask of number patterns to check. * is a repeated number and N is 0-9
# print(a)
# last_digit = [1,3,7,9]

# numbers_to_check = []
# for i in range(0, len(a)):
#     for last in last_digit:
#         for n1 in range(0,10):
#             for n2 in range(0,10):
#                 # for n3 in range(0,10):
#                     # For each mask in the list make a number where * is replaced by 0-9 and N is replaced by 0-9
#                 repeated_set = []
#                 for repeated_digit in range(0,10):
#                     # For each repeated digit make a 3 digit number from a where * is replaced by repeated_digit
#                     number = [0,0,0,0,0,0]
#                     for index, digit in enumerate(a[i]):
#                         # If index is 0 and repeated_digit is 0 or n1 is 0 or n2 is 0 or n3 is 0 then skip
#                         if digit == "*":
#                             number[index] = repeated_digit
#                         elif digit == "N1":
#                             number[index] = n1
#                         elif digit == "N2":
#                             number[index] = n2
#                         # elif digit == "N3":
#                         #     number[index] = n3
#                     number[5] = last
#                     #if len(str(int("".join(map(str,number))))) == 6:
#                     repeated_set.append(number)
#                 primes = 0
#                 # For each array turn each member into a number and check if it's prime
#                 for number in repeated_set:
#                     number = int("".join(map(str,number)))
#                     if len(str(number)) == 6:
#                         if is_prime(number):
#                             primes += 1
#                 if primes == 8:
#                     print(f"Found 8 primes in the group {repeated_set}")
#                     break
### This is how it was actually solved ###

# BUT I thought how hard is it to make a more generic method that can do this for any number of digits and any number of repeats

def get_combos(number_of_repeats, number_of_numbers):
    # Create a list of all the possible combinations of numbers and stars, add a digit to the end of each N to make it unique
    combos = []
    # Add a star to combos for each repeat
    for i in range(0, number_of_repeats):
        combos.append("*")
    # Add a number to combos for each number with a unique digit at the end
    for i in range(0, number_of_numbers):
        combos.append(f"N{i}")

    combos_all = list(perm_unique(combos))
    return combos_all

# Try making a generic function for this
def find_primes_in_length(digits, number_of_primes):
    # Start with number of repeats set to 2 and number of numbers set to digits - 2 - 1
    number_of_repeats = 2
    number_of_numbers = digits - 2 - 1

    for i in range(0, digits - 3):
        combos_all = get_combos(number_of_repeats, number_of_numbers)
        keep_going = run_combos_all(combos_all, digits, number_of_numbers, number_of_primes)
        if not keep_going:
            break
        print(f"Number of repeats: {number_of_repeats}, Number of numbers: {number_of_numbers}")
        number_of_repeats += 1
        number_of_numbers -= 1

def run_combos_all(combos_all, digits, number_of_numbers, number_of_primes):
    last_digit = [1,3,7,9]
    for combo in range(0, len(combos_all)):
        for last in last_digit:
            numbered_masks = []
            # For each n in combo loop through 0-9 and replace N{0-9} with n
            for n in range(0,10**number_of_numbers):
                number = []
                for index, digit in enumerate(combos_all[combo]):
                    number.append(digit)
                # For each repeated digit make a 3 digit number from combos_all where * is replaced by repeated_digit
                if len(str(n)) < number_of_numbers:
                    n = str(n).zfill(number_of_numbers)
                else:
                    n = str(n)
                for index, digit in enumerate(number):
                    if digit.startswith("N"): # This isn't working because it can only hit one of the N values. Need to set them all then loop through each repeated item
                        number[index] = n[int(digit.replace("N",""))]
                number.append(last)
                numbered_masks.append(number)

            # Now we have a list of all the masks to check. Now we need to loop through each mask and check if it's prime
            for maski, mask in enumerate(numbered_masks):
                repeated_set = []
                for repeated_digit in range(0,10):
                    repeated_number = mask.copy()
                    for index, digit in enumerate(combos_all[combo]):
                        # If index is 0 and repeated_digit is 0 or n1 is 0 or n2 is 0 or n3 is 0 then skip
                        if digit == "*":
                            repeated_number[index] = repeated_digit
                    repeated_set.append(repeated_number)
                primes = 0
                # For each array turn each member into a number and check if it's prime
                for r in repeated_set:
                    number = int("".join(map(str,r)))
                    if len(str(number)) == digits:
                        if is_prime(number):
                            primes += 1
                if primes == number_of_primes:
                    print(f"Found {number_of_primes} primes in the group {repeated_set}")
                    return False
    return True

find_primes_in_length(6, 8)