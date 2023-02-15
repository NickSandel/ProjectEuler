# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# Time the following code
import time
start = time.time()

def is_pandigital(multiplicand, multiplier, product):
    # Turn the numbers into a list of digits
    multiplicand = sorted(map(int, str(multiplicand)))
    multiplier = sorted(map(int, str(multiplier)))
    product = sorted(map(int, str(product)))
    # Add the digits together
    digits = multiplicand + multiplier + product
    # It actually only wants where it's 1 through 9 so if the list is shorter than 9 then it's not pandigital. Remove this if it's 1 through n
    if len(digits) != 9:
        return False
    # Check if the digits are pandigital by ordering them and checking if they are the same as the digits 1 to n
    digits = sorted(digits)
    for i, d in enumerate(digits):
        if d != i + 1:
            return False
    return True

# Iterate through all 2 digit and 4 digit numbers multiplying them together and checking if the result is pandigital
# I think I can do this with a single loop and just check if the result is pandigital and if it is then add it to a list
# Then I can just sum the list
pandigital_products = []
for multiplacand in range(1,99):
    for multiplier in range(1,9999):
        product = multiplacand * multiplier
        if is_pandigital(multiplacand, multiplier, product):
            print(multiplacand, multiplier, product)
            if product not in pandigital_products:
                pandigital_products.append(product)

print(pandigital_products)
print(sum(pandigital_products))

# Print the time taken to run the code
print(time.time() - start)

# Answer: 45228

# Try this again but go for permutations instead of checking if it's pandigital
# I think I can do this by generating all the permutations of 1 to 9 and then checking if there is a valid multiplication present

start = time.time()
import itertools
permutations = itertools.permutations(range(1,10))

# I can cheat because from my solution I know the last 4 digits will be the product
pandigital_products = []
for perm in permutations:
    product = int(''.join(map(str, perm[-4:])))
    # Check the combinations of the first 5 digits but I only need to separate them into 1 and 4 and 2 and 3 pairs

    multiplicand = int(''.join(map(str, perm[0:1])))
    multiplier = int(''.join(map(str, perm[1:5])))
    if multiplicand * multiplier == product:
        print(multiplicand, multiplier, product)
        if product not in pandigital_products:
                pandigital_products.append(product)


    multiplicand = int(''.join(map(str, perm[0:2])))
    multiplier = int(''.join(map(str, perm[2:5])))
    if multiplicand * multiplier == product:
        print(multiplicand, multiplier, product)
        if product not in pandigital_products:
                pandigital_products.append(product)

print(pandigital_products)
print(sum(pandigital_products))
print(time.time() - start) # This method is significantly faster