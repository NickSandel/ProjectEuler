# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# Observations:
# There must be some sensible upper limit to adhere to here 9! = 362,880
# I'm not sure how to discern where the upper limit is though as surely I could have some number like 990077 which fits?
# Ooh maybe that's it the upper limit is 999,999??? Or maybe it's 2,540,160 because that's equal to 9! * 7 but that does say the limit is lower 
# because 9,999,999 to the factorialised sum equals that value and any higher numbers can't consist then of digits factorialised adding to it

# I wonder if there's a smarter permutation way to tackle this one instead of brute forcing the numbers instead work through the combinations of factorials
# There will also be some base logic here where there's no point checking if 111 is a match as none of the digits can add up to 3 digits
# However as the top number isn't unreasonable I could just brute force it...
import math

curious_numbers = []
for i in range(3,2540160):
    sum_factorial = sum([math.factorial(int(x)) for x in str(i)])
    if i == sum_factorial:
        curious_numbers.append(i)

print(sum(curious_numbers))