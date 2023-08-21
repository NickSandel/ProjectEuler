"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""
import math

fractions = []

# Ha there is a clear pattern at play. Take the previous denominator, multiply by 2 and then add the one before to get the new one. 
# Then for the numerator multiply by previous denominator and add new numerator
fractions.append([0,1])
fractions.append([3,2])

for i in range(2, 1001):
    denominator = fractions[i-1][1] * 2 + fractions[i-2][1]
    numerator = fractions[i-1][1] + denominator
    fractions.append([numerator, denominator])

def count_digits(number):
    if number > 0:
        digits = int(math.log10(number))+1
    elif number == 0:
        digits = 1
    return digits

answer = 0
for fraction in fractions:
    if count_digits(fraction[0]) > count_digits(fraction[1]):
        answer += 1

print(answer)