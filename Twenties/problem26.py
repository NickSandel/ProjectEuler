# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# After a quick google on how to find recurring decimals in python found a link to here: https://en.wikipedia.org/wiki/Repeating_decimal#Decimal_expansion_and_recurrence_sequence
# It's hinting that the trick is to use long division and when you end up with a remainder which is the same as what you started as the numerator then you've hit the repeating patter

# Manually then for 1/3 change it to 10/3 which is 3 remainder 1 which is back where we started and will then repeat forever down the decimal chain

n = 1
d = 1


highest_repetition = 0
highest_repetition_d = 0
while d < 1000:
    d += 1
    exponent = 1
    while exponent < 1000:
        remainder = n*10**exponent%d
        if remainder == 0:
            print(f'D {d} has no remainder so does not repeat')
            break
        elif remainder == 1:
            if exponent > highest_repetition:
                highest_repetition = exponent
                highest_repetition_d = d
            print(f'D {d} does repeat and has {exponent} repeating digits {n/d}')
            break
        exponent += 1
print(f'Highest repeating d is {highest_repetition_d}')

# Hmm this is trickier I had hoped to be able to easily find those with repeating and then manually find the pattern or not. 
# I think I need to be smarter and go through that long division step process
# I can cut out any number ending 0 as a starter