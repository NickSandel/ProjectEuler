# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.
from math import sqrt

print(sqrt(1929394959697989990))
#1389026623.1062636

print(sqrt(1020304050607080900))
#1010101010.1010101

# Ok so the number is in this range. I could brute force one way or another to find it...
# For brute force it's just a case of iterating through those place numbers until a whole number is found from rooting it
# Or is it less combinations to go through the range I have?
# 1,389,026,623

print(1389026623 - 1010101010)
# 330,105,403
# One tenth of this
# The other way round is 9! which is 362,880 so actually that way will be much more efficient

# I could write a horribly messy nested loop 9 layers deep but would rather not frankly

def check_square_form(number):
    s = str(number)
    if (s[0] == '1' and s[2] == '2' and s[4] == '3' 
        and s[6] == '4' and s[8] == '5' and s[10] == '6' 
        and s[12] == '7' and s[14] == '8' and s[16] == '9' and s[18] == '0'
        ):
        return True
    else:
        return False
    
print(check_square_form(1929394959697989990))
print(check_square_form(1020304050607080900))
print(check_square_form(1121314151617181919))

# Trying to figure out the permutations is giving me a headache so I'll brute force between the range instead!

start = 1010101010
end = 1389026623

while start < end:
    checknumber = start * start
    if (check_square_form(checknumber)):
        print("Winner:")
        print(start)
        break
    start += 10 # 10 as the resulting number must end in 0

# This was a bit slow but still got the right result

# Winner:
# 1389019170