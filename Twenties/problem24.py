# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Start with 1, 2, 3, 4 to flesh out logic
# 1234 1243 1324 1342 1423 1432 2134 2143 2314 2341 2413 2431 3124 3142 3214 3241 3412 3421 4123 4132 4213 4231 4312 4321
# 4! = 4*3*2*1 = 24 terms
# Each starting number has 6 possibles behind it which is 3! = 3*2*1 = 6 also means then that you can break into groups of 6 to find the starting number 
# So if I wanted to find the 8th term I would ignore 1 as it only goes up to 6, 3 would start at 12 so it must begin with a 2. 
# Then I can tell the next number batching is 2! and 8 will be the first batch which means the next number is 1 so it starts 21 
# then it must be the higher of the remainder digits as it's the last from 2! group so 3 then 4 so 2134 should be 8th term
# What about 21st term? So again start with batches of 6 (3!) 21/6 rounded up is 4 this means the 4th group so it begins 4 
# then it's 3rd in that group of 6 because 21 - (3!(6)*3(4th group minus 1)) = 3 or 21%6 = 3 remainder. 3/2 rounded up is 2 so it's the second higest number next which is 2 so 42 
# then it's 1st in that group of 2 because 3 (remainder from previous step) - (2!(2)*1(2nd group minus 1)) = 2. 3 - 2 = 1 so it's the lowest number next 421 followed by 3 
# so 4213 should be 21st term

# For the problem it is 10! which is 10*9*8*7*6*5*4*3*2*1 = 3,628,800 terms

# Try and code my logic above for 1,2,3,4
import math
def lexical_at_position(numbers, position):
    numbers = sorted(numbers)
    print(numbers)
    number_of_items = len(numbers)
    total_terms = math.factorial(number_of_items)
    print(total_terms)
    items_left = position
    for i in range(1, number_of_items+1):
        if len(numbers) == 1:
            #Stop looping you've only got one left!
            print(f"Number {i} is {numbers[0]}")
            break

        number_index = math.ceil(items_left/math.factorial(number_of_items-i))
        # Now work with the remainder
        items_left = items_left%math.factorial(number_of_items-i)
        print(f"Number {i} is {numbers[number_index-1]}")
        # Get rid of a number when it's been consumed, this will leave the rest of the list ordered properly
        numbers.pop(number_index-1)


numbers = [4,2,1,3]
lexical_at_position(numbers, 15)


numbers = [0,1,2,3,4,5,6,7,8,9]
lexical_at_position(numbers, 1000000)