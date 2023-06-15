# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
 
# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196 never produce a palindrome. 
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
# Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. 
# In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, 
# with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty 
# iterations before producing a palindrome: 
# 4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994

# How many Lychrel numbers are there below ten-thousand?

# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

from common.helpers import is_palindrome

lychrel_numbers = 0
for i in range(1,10000):
    # Add i to its reverse
    res = i + int(str(i)[::-1])
    # Check if it's a palindrome
    # If it is, break
    # If it isn't, add it to its reverse and repeat
    if is_palindrome(res):
        # print(f"{res} is a palindrome")
        continue
    else:
        # print(f"{res} is not a palindrome")
        b = res
        is_p = False
        for x in range(1,50):
            b += int(str(b)[::-1])
            if is_palindrome(b):
                # print(f"{b} is a palindrome")
                is_p = True
                break
            # else:
            #     print(f"{i} is not a palindrome")
            x += 1
        if is_p:
            continue      

    # If it's not a palindrome after 50 iterations, it's a Lychrel number
    # So add 1 to the Lychrel number counter
    print(f"{i} is a Lychrel number")
    lychrel_numbers += 1

print(f"There are {lychrel_numbers} Lychrel numbers below 10,000")
    