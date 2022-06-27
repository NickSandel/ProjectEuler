# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# start_num = 13
# print(start_num)

# num = start_num
# chain = 1
# while num > 1:
#     if num % 2 == 0: # num is even
#         num = num / 2
#         chain += 1
#         print(num)
#     else: # num is odd
#         num = 3 * num + 1
#         chain += 1
#         print(num)
# print("Num ", start_num, " has chain length ", chain)

def collatz(start_num):
    num = start_num
    chain = 1
    while num > 1:
        if num % 2 == 0: # num is even
            num = num / 2
            chain += 1
        else: # num is odd
            num = 3 * num + 1
            chain += 1
    return chain

from helpers import is_prime

largest_chain = 0
largest_chain_num = 0
for a in range(1, 1000000):
    chain = collatz(a)
    if chain > largest_chain:
        largest_chain = chain
        largest_chain_num = a

print("Largest chain ", largest_chain, " for ", largest_chain_num)