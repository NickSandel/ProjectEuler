# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# Don't need to build the matrix just need to build the corners then add them all up
# Formula for each corner is:
# - Top right: square side ** 2
# - Top left: square side ** 2 - (square side - 1)
# - Bottom left: square side ** 2 - (square side * 2 - 2)
# - Bottom right: square side ** 2 - (square side * 3 - 3)
# Iterate down the square sizes which will drop the square side value down 2 each iteration

# Ok let's try it!

square_side = 1001
values = [1]
while square_side > 1:
    values.append(square_side ** 2)
    values.append(square_side ** 2 - (square_side - 1))
    values.append(square_side ** 2 - (square_side * 2 - 2))
    values.append(square_side ** 2 - (square_side * 3 - 3))
    square_side -= 2

# print(values)
print(sum([int(x) for x in values]))