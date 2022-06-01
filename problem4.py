# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# First detect if a number is a palindrome:
def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


# Largest from product of 2 3 digit numbers
# Start both at 999 and walk backwards?
palindromes = []
n1 = 999
found = False
while n1 > 100:
    for n2 in range(999, 100, -1):
        product = n1 * n2
        if is_palindrome(product):
            pal = [n1, n2, product]
            palindromes.append(pal)
        n2 -= 1
    n1 -= 1

print(sorted(palindromes, key=lambda x:x[2], reverse=True)[0])
# This did find A palindrome but I wonder if it's not the largest because of how I walked backwards in the loops... let's get all palindromes then find the largest pair which caused it