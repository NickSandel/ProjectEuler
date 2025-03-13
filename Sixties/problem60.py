#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from common.helpers import is_prime, SieveOfEratosthenes

# Get primes below 50,000 (guessed starting point to work up to)
primes = sorted(SieveOfEratosthenes(30000))
primes_reference = []#sorted(SieveOfEratosthenes(10000000))

# I have a bunch of primes but how to iterate through them to find the set I want?
def check_set_prime (prime_set, primes_check):
    concat_primes = []
    for i in range(len(prime_set)):
        for ii in range(len(prime_set)):
            if i != ii:
                concat_primes.append(int(str(prime_set[i]) + str(prime_set[ii])))
                concat_primes.append(int(str(prime_set[ii]) + str(prime_set[i])))

    # This method is much quicker than checking a subset of a bunch of primes!
    valid = True
    for prime in concat_primes:
        if not is_prime(prime):
            valid = False
            break
    return valid
    #if set(concat_primes).issubset(primes_check):
        # return True

prime_set = [3,7,109,673]

check_set_prime(prime_set, primes_reference)

# The real challenge now is generating the sets and iterating over them
# I wonder if something can be done in how it's iterated over to optimise this
# Something like start with the smallest prime and add to it's set until the lowest combination can be found
# Maybe also store pairs which can't go together to make unique primes? Or maybe just run through pairs first and then find the common ground?

# invalid_pairings = []
# prime_set_length = 4
# def brute_force():
#     # Maybe brute force it?
#     for i in range(len(primes)):
#         for ii in range(i+1,len(primes)):
#             for iii in range(ii+1,len(primes)):
#                 for iv in range(iii+1,len(primes)):
#                     prime_test = [primes[i], primes[ii], primes[iii], primes[iv]]
#                     if check_set_prime(prime_test, primes_reference):
#                         print(f"Set {prime_set} concatenated are all primes")
#                         return

# brute_force()

# Brute forcing is clearly very inefficient and a BAD IDEA

# Maybe check for all valid pairs first?
# This is the slowest part, once pairs are established it's fairly quick to go through the other sets.
# How can this be optimised?
valid_pairings = []
for i in range(len(primes)):
    for ii in range(i+1,round((len(primes))/2)): # Only go halfway as we don't need both sides of the pairing?
        prime_test = [primes[i], primes[ii]]
        if check_set_prime(prime_test, primes_reference):
            valid_pairings.append(prime_test)

print(len(valid_pairings))
# Not too bad to run this actually even though the dataset is smaller than I'd like. Gives 55611 pairs.

valid_triplets = []
# Maybe then go through each pair and check if adding in 
for i in range(len(valid_pairings)):
    for ii in range(i+1, len(valid_pairings)):
        if [valid_pairings[i][0]] == [valid_pairings[ii][0]]:
            prime_test = [valid_pairings[i][0], valid_pairings[i][1], valid_pairings[ii][1]]
            if check_set_prime(prime_test, primes_reference):
                valid_triplets.append(prime_test)
        else:
            break

print(len(valid_triplets))

valid_quads = []
# Maybe then go through each pair and check if adding in 
for i in range(len(valid_triplets)):
    for ii in range(i+1, len(valid_triplets)):
        if [valid_triplets[i][0]] == [valid_triplets[ii][0]] and [valid_triplets[i][1]] == [valid_triplets[ii][1]]:
            prime_test = [valid_triplets[i][0], valid_triplets[i][1], valid_triplets[i][2], valid_triplets[ii][2]]
            if check_set_prime(prime_test, primes_reference):
                valid_quads.append(prime_test)
        else:
            break

print(len(valid_quads))

valid_pents = []
# Maybe then go through each pair and check if adding in 
for i in range(len(valid_quads)):
    for ii in range(i+1, len(valid_quads)):
        if [valid_quads[i][0]] == [valid_quads[ii][0]] and [valid_quads[i][1]] == [valid_quads[ii][1]] and  [valid_quads[i][2]] == [valid_quads[ii][2]] :
            prime_test = [valid_quads[i][0], valid_quads[i][1], valid_quads[i][2], valid_quads[i][3], valid_quads[ii][3]]
            if check_set_prime(prime_test, primes_reference):
                valid_pents.append(prime_test)
        else:
            break

print(len(valid_pents))
for pent in valid_pents:
    print(pent)
    print(sum(pent))

# This method is very clunky and show and I'm sure could be better but I'm not sure how yet...
# It's also been a bit of trial and error to figure out which prime set to test and how high to test against.
# This was SLOW but got me the right answer of set:
# [13, 5197, 5701, 6733, 8389]
# With Sum: 26033