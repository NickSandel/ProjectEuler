# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

# Python may actually be able to handle such silly big numbers but this might miss the point... 
# to get the last 10 digits I don't need all the other digits so even if I do brute force I don't need to add all of the numbers just the last 10 digits of each

sum = 0
for i in range(1,1001):
    square = i**i
    if square > 999999999:
        sum += int(str(square)[-10:])
    else:
        sum += square
print(sum)