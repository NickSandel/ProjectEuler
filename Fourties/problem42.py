# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Easiest way might be to generate a set of triangular numbers up to a reasonable size and then iterate the words and check if any match
# Harder would be to check each incoming number to see if it's triangular without having to check the numbers one by one
# i.e. there's a shortcut way to take any number and see if it is triangular

import string

words = []
with open('Fourties\p042_words.txt', 'r') as f:
    words = f.read().split(',')
    words = [word.strip('"') for word in words]

print(len(words))
# Print largest length word
print(max([len(word) for word in words]))
# 14

# So if the largest words is 14 characters and the largest letter can be 26 the largest triangular number needed to check is 14*26=364

triangular_numbers = []
index = 1
while 1==1:
    new_number = 0.5*index*(index+1)
    # Stop loop if new number is greater than 364
    if new_number > 364:
        break
    else:
        triangular_numbers.append(int(new_number))
    index += 1

print(triangular_numbers)

# Function to score words based on their alphabetical place
def score_word(word:str) -> int:
    score = 0
    for char in word:
        score += string.ascii_lowercase.index(char.lower()) + 1
    return score

print(score_word('SKY'))

triangular_word_count = 0
for word in words:
    if score_word(word) in triangular_numbers:
        triangular_word_count += 1

print(triangular_word_count)
