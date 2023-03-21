# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

# Pythagoras! For a right angled triangle the square of the hypotenuse (side opposite the right angle) is equal to the sum of the squares of the other 2 sides
# 3**2 + 4**2 = 5**2 is the classic example

# Ok so this is all about finding the value which decomposes down to three values which when squared add up properly. 
# The ratio isn't a clean 5:4+3 one as the examples show but there will be sensible limitations to impose here 
# like I can't image a right angled triangle would be able to have a side of 1 with the other sides being integers 
# because of the way squaring works in the curve of it the next integer square will always be more than 1 higher than the last 
# and we can't have 1**2 + 1**2 = 1**2 so neither will combos like 499**2 + 1**2 = 500**2 exist

# Brute force doesn't seem right here there must be sensible options to break it down and I don't know if brute force can apply.
# I think start with the highest divisible number of 12 < 1000 which is 83*12=996 as the golden ratio must exist in there 
# then maybe step up and down the hypotenuse value to tell if there are more combinations?

def count_combos(p:int):
    # First find the golden ratio from this p and check it adds up
    a = (p / 12) * 3
    b = (p / 12) * 4
    c = (p / 12) * 5
    count = 0
    if a**2 + b**2 == c**2:
        # print(f"a: {a}, b: {b}, c:{c}")
        count += 1

    # Maybe the hypotenuse can never get shorter but it can get longer?
    c2 = c
    while c2 < p:
        c2 += 1
        a2 = a - (c2-c)
        b2 = b
        while b2 < c2 and a2 > 1:
            b2 += 1
            a2 -= 1
            if a2**2 + b2**2 == c2**2:
                # print(f"a: {a2}, b: {b2}, c:{c2}")
                count += 1

    return count

print(count_combos(120))
print(count_combos(1200))

p = 1000
highest_combo_p = 0
while p > 0:
    if p % 12 == 0:
        combos = count_combos(p)
        if combos > highest_combo_p:
            highest_combo_p = combos
            print(f"New highest combo with combos = {combos} from p {p}")
    p -= 1

print(highest_combo_p)