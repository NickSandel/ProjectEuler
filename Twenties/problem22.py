# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
import string
# This gets alphabetical position quite nicely
# print(string.ascii_lowercase.index('a') + 1)

data = []
with open('Twenties\p022_names.txt', 'r') as f:
    for line in f.readlines():
        names = line.split(',')
        for name in names:
            name = name.replace('"', '')
            data.append(name)
# Sort the data
data.sort()

def score_name(name):
    name_score = 0
    for char in name.lower():
        name_score += string.ascii_lowercase.index(char) + 1
    return name_score

total_score = 0
for i in range(len(data)):
    total_score += score_name(data[i]) * (i+1)

print(total_score)