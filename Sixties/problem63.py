# The 5-digit number, 16807 = 7 ** 5, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8 ** 9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

# Check for limitations
# 10 ** 1 = 10, 10 ** 2 = 100 so 10 is too high
# 9 ** 2 = 81, 9 ** 3 = 729 so this one can keep going
# 2 ** 1 = 2, 2 ** 2 = 4 so stops
# For each integer 2 to 9 need to determine where the power stops and count instances as this only considers whole integers

counter = 0
for i in range(1, 10):
    stop = False
    start = 1
    while stop == False:
        if len(str(i ** start)) == start:
            start += 1
            counter += 1
        else:
            print(f"Number {i} stops at {start}")
            stop = True

print(f"Counter = {counter}")