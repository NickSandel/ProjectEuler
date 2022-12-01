from math import sqrt, floor
import time

start = time.time()

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

# How many abundant numbers are there below the threshold given?
abundants_even = []
abundants_odd = []
for i in range(1, 28123 + 1):
    if is_abundant(i):# and i % 2 != 0: # There are odd ones but really not many!
        if i % 2 == 0:
            abundants_even.append(i)
        else:
            abundants_odd.append(i)

# I got stuck with brute forcing so looked at some patterns in the brute force approach up to 1000
# 945 is the smallest odd abundant number so all odd numbers less than 945 + 12 = 957 are included in the sum I want
# 46 is the smallest even number which cannot be made from the sum of abundant numbers

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
                    can_pair = True
                    break
    
    if can_pair is False:
        sum_non_abundant += i

end = time.time()
print(sum_non_abundant)
print(f"Program took this long: {end-start}")