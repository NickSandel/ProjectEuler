# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Clearly start with all 4 digit ones to prove this out

def is_power_of_digits(number, power):
    powered_digits = 0
    for n in str(number):
        powered_digits += int(n) ** power
    if powered_digits == number:
        return True
    else:
        return False

print(is_power_of_digits(1634, 4))
print(is_power_of_digits(1635, 4))
print(is_power_of_digits(8208, 4))
print(is_power_of_digits(9474, 4))

sum_powered_numbers = 0
for i in range(1111, 9999):
    if is_power_of_digits(i, 4):
        sum_powered_numbers += i
        print(i)

print(f'Overall sum is: {sum_powered_numbers}')

sum_powered_numbers = 0
for i in range(2, 999999):
    if is_power_of_digits(i, 5):
        sum_powered_numbers += i
        print(i)

print(f'Overall sum is: {sum_powered_numbers}')