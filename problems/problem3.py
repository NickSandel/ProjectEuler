# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ? 600,851,475,143

# Find all divisors first then figure out if they're prime?
# Cut out all of the even numbers to speed it up?
# 150212868786 is 1/4 of 600851475143 because there's no point trying to go higher than halfway and then no point looking at even numbers when I'm after primes so why even process those?


# for num in range(2, 150212868786):
#     if 600851475143 % (num * 2 - 1) == 0:
#         print(num * 2 - 1)

bignum = 600851475143
divisors = []
for r in range(2, round(bignum/4)):
    if bignum % (r * 2 - 1) == 0: # This is cool, gets you onto the odd numbers only
        divisors.append(r * 2 - 1)
        if len(divisors) > 1:
            if divisors[len(divisors)-1] * divisors[len(divisors)-2] == bignum:
                break

for i in range(len(divisors)-2):
    print(divisors[i])
    divisors.append(int(bignum/divisors[i]))

print(divisors)

# Find out which divisors are primes
not_primes = []
for divisor in divisors:
    for x in range(2, round(divisor/4)):
        if divisor % (x * 2 - 1) == 0:
            print("Not prime:" + str(divisor))
            not_primes.append(divisor)
            break

# Print difference then just manually pick the largest :)
print(list(set(divisors).difference(not_primes)))

# divisors are:
# could I have reached this point sooner by finding the halfway divisor? The program was still hammering away past the 8462696833 mark but 
# I stopped it because I could see /71 was equal to that so I knew there would be no larger divisor found
71
839
1471
6857
59569
104441
486847 # Could I have stopped it here in some magical knowledge that I was halfway?
1234169 # Maybe stopped it here actually as that's more reasonable?
5753023
10086647
87625999
408464633
716151937
8462696833

71, 
839, 
1471, 
6857, 
59569, 
104441, 
486847, 
1234169, 
8462696833, 
716151937, 
408464633, 
87625999, 
10086647, 
5753023