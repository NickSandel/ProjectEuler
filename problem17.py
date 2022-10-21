# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

# Which words will be used:
# Ones: [one, two, three, four, five, six, seven, eight, nine]
# Teens: [ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]
# Eys: [ten, twenty, thirty, fourty, fifty, sixty, seventy, eighty, ninety]
# Past 20 it's Eys + ones
# Hundrededs = ones + hundred + and
# There will be clear compounding to help here. Like once you've done the counts for one set of 100 you can apply that to 200 with the difference being the first word
# Will be just one [one thousand]

# Brute force to hammer through and do this? Nah I think we can be more finessed than that surely... might even have to as note sure how to brute force it!

len_ones = 0
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in range(1,9+1):
    len_ones += len(ones[i-1])

print(len_ones)
#36

len_teens = 0
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
for i in range(1,9+2):
    len_teens += len(teens[i-1])

print(len_teens)
#78

len_ees = 0
ees = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#Go through 20 : 90
for i in range(20, 90 + 10, 10):
    # Here need to take the number, multiply its length by 10 and add the sum of len_ones
    len_ees += len(ees[int(i/10)-2]) * 10 + len_ones

print(len_ees)
#46 for just the ees
#748 when adding ones and * 10

# Lengths up to 100 (1-99)
pre_hundred = len_ones + len_teens + len_ees
print(pre_hundred)

# 748 looks correct for pre len ees as it is (46 * 10) + (36 * 8) or ees_length * 10 (one ee for each digit) + len_ones * 8 (8 because of 20 to 90 being 8 iterations)
# Pre hundred then should be 748 + 70 + 36 = 854

# To sum it all separately 1-9 (for hundreds) * 100 = 36 * 100 = 3600 1-99 * 9 = 854 * 9 = 7686, "hundred" * 9 = 63, "hundredand" * 999 = 8910 == 3600+7686+63+99 = 20259 + 11 = 21124