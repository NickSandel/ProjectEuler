# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

denominator = 99
numerator = 98

values = []

for d in range(denominator, 12, -1):
    d_str = str(d)
    if d_str[0] == d_str[1]:
        continue
    for n in range(d - 1, 11, -1):
        n_str = str(n)
        if n_str[0] == n_str[1]:
            continue
        if d_str[0] in n_str or d_str[1] in n_str:
            # print(f"n {n} and d {d} viable to check")
            d_no_0 = d_str.replace(d_str[0],"")
            n_no_0 = n_str.replace(d_str[0],"")
            if d_no_0 != "0" and n_no_0 != "0":
                if int(n_no_0)/int(d_no_0) == n/d:
                    print(f"Found one! N:{n}, D:{d}")
                    values.append([n,d])

            if d_str[1] != "0":
                d_no_1 = d_str.replace(d_str[1],"")
                n_no_1 = n_str.replace(d_str[1],"")
                if d_no_1 != "0" and n_no_1 != "0":
                    if int(n_no_1)/int(d_no_1) == n/d:
                        print(f"Found one! N:{n}, D:{d}")
                        values.append([n,d])
                        
# Now I need to find the lowest common denominator of the values
print(values)

# To find the lowest demoninator I could multiply all the denominators together and then divide by the greatest common denominator of the numerators
largest_numerator = 1
largest_denominator = 1
for v in values:
    largest_numerator *= v[0]
    largest_denominator *= v[1]

print(f"largest_numerator {largest_numerator}, largest_denominator {largest_denominator}")

# Just by looking I can see this lowest common denominator is 100
# But I'll write a function to find it
def greatest_common_denominator(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_1 = greatest_common_denominator(largest_numerator, largest_denominator)
print(f"lowest common denominator {largest_numerator/gcd_1} / {largest_denominator/gcd_1}")