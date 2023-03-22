# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# The decimal part is a complete distraction because dn is an integer so it's not about multiplying massive decimals together!

# I don't think I actually need to build the number to be able to figure this out but maybe I will start with that

val = ""
for i in range(1,300000):
    val += str(i)

print(val[0])
print(val[9])
print(val[99])
print(val[999])
print(val[9999])
print(val[99999])
print(val[999999])
print(len(val))

# No need to get too smart on this one the brute force approach worked
# I set the above range until it hit a large enough array and then I can run this multiplcation
print(int(val[0])*int(val[9]) * int(val[99]) * int(val[999]) * int(val[9999]) * int(val[99999]) * int(val[999999]))

# I can predict the length of the output based on how many digits it spans to
# Up to 99:
print(9 + (90 * 2))
print(9 + (90 * 2) + (900 * 3))
print(9 + (90 * 2) + (900 * 3) + 9000 * 4)

# As I got the answer with brute force not pursuing this further