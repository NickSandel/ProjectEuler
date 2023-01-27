# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

# Hmm ok seems like 2 ways to tackle this:
# 1) Iterate through loads of numbers until you find the pattern
# 2) Generate primes and look for the pattern. Is there any point starting too low?
import sys
 
# setting path
sys.path.append('../Euler')
from common.helpers import SieveOfEratosthenes
# As usual start with the examples
primes = SieveOfEratosthenes(99)
# Remove single digit primes
primes = [prime for prime in primes if prime > 10]

# Group the primes by the last digit
# primesByLastDigit = {}
# for prime in primes:
#     lastDigit = str(prime)[-1]
#     if lastDigit in primesByLastDigit:
#         primesByLastDigit[lastDigit].append(prime)
#     else:
#         primesByLastDigit[lastDigit] = [prime]

# # Show highest count group
# highestCount = 0
# highestCountGroup = None
# for group in primesByLastDigit:
#     if len(primesByLastDigit[group]) > highestCount:
#         highestCount = len(primesByLastDigit[group])
#         highestCountGroup = group

# print(f"Highest count group: {highestCountGroup} with {highestCount} primes {primesByLastDigit[highestCountGroup]}")

# # Now look for the pattern in 5 digit numbers
# primes = SieveOfEratosthenes(99999)

# # Remove up to 4 digit primes
# primes = [prime for prime in primes if prime > 1000]

# # Group the primes by the last digit
# primesByLastDigit = {}
# for prime in primes:
#     lastDigit = str(prime)[-1]
#     if lastDigit in primesByLastDigit:
#         primesByLastDigit[lastDigit].append(prime)
#     else:
#         primesByLastDigit[lastDigit] = [prime]

# # Show highest count group
# highestCount = 0
# highestCountGroup = None
# for group in primesByLastDigit:
#     if len(primesByLastDigit[group]) > highestCount:
#         highestCount = len(primesByLastDigit[group])
#         highestCountGroup = group

# # Now run through the groups and create sub groups which have repeated digits
# prime_subgroups = {}
# # Seed the subgroups with the last digit groups
# for group in primesByLastDigit:
#     prime_subgroups[group] = {}

# print(prime_subgroups)

# # Now iterate through the primes in the group and look for at least 2 digits being the same and add them to the subgroups
# for group in primesByLastDigit:
#     for prime in primesByLastDigit[group]:
#         primeString = str(prime)
#         for i in range(0, len(primeString)):
#             for j in range(i+1, len(primeString)):
#                 if primeString[i] == primeString[j]:
#                     if primeString[i] in prime_subgroups[group]:
#                         prime_subgroups[group][primeString[i]].append(prime)
#                     else:
#                         prime_subgroups[group][primeString[i]] = [prime]

# print(prime_subgroups)

# I wonder if I am just attacking this the wrong way. What if I use a set length of digits and then look for the pattern in that?
# It must end with a 1,3,7 or 9 to be prime so why not set patterns and look for how many primes fit that pattern?
from common.helpers import is_prime

# Start with the 5 digit numbers
# Patterns for 3 fixed digits and 2 repeating:
# [1-9][0-9][*][*][1,3,7,9]
# [1-9][*][0-9][*][1,3,7,9]
# [1-9][*][*][0-9][1,3,7,9]
# [*][0-9][*][0-9][1,3,7,9]
# [*][*][0-9][0-9][1,3,7,9]
# How many combos where last digit is fixed and at least 2 others have to be fixed? But the rest can be 0-9
largest_group = []
for last_digit in [1,3,7,9]:
    # Fix the first 2 digits
    for first_digit in range(1,10):
        for second_digit in range(0,10):
            group_1 = []
            group_2 = []
            group_3 = []
            # Now fix the last 2 digits
            for repeated_digit in range(0,10):
                number = int(f"{first_digit}{second_digit}{repeated_digit}{repeated_digit}{last_digit}")
                if is_prime(number):
                    group_1.append(number)
                number = int(f"{first_digit}{repeated_digit}{repeated_digit}{second_digit}{last_digit}")
                if is_prime(number):
                    group_2.append(number)
                number = int(f"{first_digit}{repeated_digit}{second_digit}{repeated_digit}{last_digit}")
                if is_prime(number):
                    group_3.append(number)

            if len(group_1) > len(largest_group):
                largest_group = group_1
            if len(group_2) > len(largest_group):
                largest_group = group_2
            if len(group_3) > len(largest_group):
                largest_group = group_3

print(largest_group)
# Fuck me this worked!

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


# Now let's try with a 6 digit number
# How many combos where last digit is fixed and at least 2 others have to be fixed? But the rest can be 0-9
a = list(perm_unique(["*","*","*","N1","N2"]))
# This is the mask of number patterns to check. * is a repeated number and N is 0-9
print(a)
last_digit = [1,3,7,9]

numbers_to_check = []
for i in range(0, len(a)):
    for last in last_digit:
        for n1 in range(0,10):
            for n2 in range(0,10):
                # for n3 in range(0,10):
                    # For each mask in the list make a number where * is replaced by 0-9 and N is replaced by 0-9
                for repeated_digit in range(0,10):
                    # For each repeated digit make a 3 digit number from a where * is replaced by repeated_digit
                    number = [0,0,0,0,0,0]
                    for index, digit in enumerate(a[i]):
                        # If index is 0 and repeated_digit is 0 or n1 is 0 or n2 is 0 or n3 is 0 then skip
                        if digit == "*":
                            number[index] = repeated_digit
                        elif digit == "N1":
                            number[index] = n1
                        elif digit == "N2":
                            number[index] = n2
                        # elif digit == "N3":
                        #     number[index] = n3
                    number[5] = last
                    #if len(str(int("".join(map(str,number))))) == 6:
                    numbers_to_check.append(number)

print(len(numbers_to_check))
for tens in range(1,int((len(numbers_to_check))/10)+1):
    primes = 0
    # For each array turn each member into a number and check if it's prime
    for number in numbers_to_check[tens*10-10:tens*10]:
        number = int("".join(map(str,number)))
        if len(str(number)) == 6:
            if is_prime(number):
                primes += 1
    if primes == 8:
        print(f"Found 8 primes in the group {numbers_to_check[tens*10-10:tens*10]}")
        # break
