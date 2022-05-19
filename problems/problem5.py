# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Is this about primes again? What are the lowest primes in 1 to 10?
# 1 2 3 5 7
# 10 = 2 * 5 
# 9 = 3 * 3  
# 8 = 2 * 2 * 2
# 4 = 2 * 2

# What do I know? The number will be > 2520, do I know an upper bound? Is it all of them multiplied together?
upper = 2*3*4*5*6*7
lower = 2*3*5*7*10

for i in range(lower, upper, 1):
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0:
        print(i)
        break

#7*5* 3*3* 2*2*2 5*2 2*2*3 3*5 2*3*3 *11*13*17*19

upper = 2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17
lower = 2*3*5*7*11*13*17*19*20

for i in range(lower, upper, 1):
    if i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0 and i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0:
        print(i)
        break

primes_to_twenty = [1, 3, 5, 7, 11, 13, 17, 19]

116396280
232792560