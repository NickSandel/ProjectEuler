# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(is_pythagorean(3,4,5))
print(is_pythagorean(6,8,10))
print(is_pythagorean(5,8,10))

# Is this just super simple in following the 3,4,5 up to numbers which add up to 1000? Surely not...
print(is_pythagorean(240,320,400))
# Close just 40 more to add in
print(is_pythagorean(249,332,415))
#I think this is the closest I can get with this scaling this pairing

# Time for some algorithmic brute force
for a in range(1,1000):
    for b in range (1,1000):
        for c in range(1,1000):
            if (a + b + c) == 1000:
                if is_pythagorean(a,b,c):
                    product = a * b * c
                    print(a)
                    print(b)
                    print(c)
                    print(product)
                    break


#Remember the answer just wants the product of the numbers not the numbers themselves!

