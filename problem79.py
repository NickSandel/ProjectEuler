# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, 
# if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

# Ok so need to find unique number combinations and add them together to find the shortest possible combo
# Order of numbers matters
# Frequency of numbers matters

# Read from keylog.txt into array

with open('problems/keylog.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# # print(lines)
# # print(lines[0][0])

# pin = list(['7', '3'])
# # Go through each line from the file
# for line in lines:
#     # Go through each number in the line
#     for digit_index, digit in enumerate(line):
#         digit_found = False
#         # Go through all digits in the pin
#         for pin_index, num in enumerate(pin):
#             # If the digit appears in the pin already ignore it
#             if digit == num:
#                 digit_found = True
        
#         # Dealing with the first unfound digit and an empty pin
#         if not digit_found:
#             if digit_index == 0 and len(pin) == 0:
#                 pin.insert(0, digit)
#             # If it is the first digit and the second is not in the pin then add this to the end
#             elif len(pin) > 0 and digit_index == 0 and line[1] not in pin:
#                 pin.append(digit)
#             # If digit is not found but the subsequent digit is found add this number in front of it
#             elif len(pin) > 0 and digit_index == 0 and line[1] in pin:
#                 pin.insert(pin.index(line[1])-1, digit)
#             # If digit is not found but the earlier digit is found add this number behind it
#             elif len(pin) > 0 and digit_index == 1 and line[0] in pin:
#                 pin.insert(pin.index(line[0])+1, digit)
#             # If digit is not found but the earlier digit is found add this number behind it
#             elif len(pin) > 0 and digit_index == 2 and line[1] in pin:
#                 pin.insert(pin.index(line[1])+1, digit)
#             else:
#                 pin.append(digit)

# print(pin)

# Another approach:
# Find the first digit
# first_digits = []
# second_digits = []
# third_digits = []
# for line in lines:
#     if line[0] not in first_digits:
#         first_digits.append(line[0])

# print(first_digits)

# for line in lines:
#     if line[1] in first_digits:
#         first_digits.remove(line[1])
#     elif line[1] not in second_digits:
#         second_digits.append(line[1])

# print(first_digits)
# print(second_digits)

# for line in lines:
#     if line[2] in second_digits:
#         second_digits.remove(line[2])
#     elif line[2] not in third_digits:
#         third_digits.append(line[2])

# print(first_digits)
# print(second_digits)
# print(third_digits)


# for line in lines:
#     if line[2] in second_digits:
#         second_digits.remove(line[2])
#     elif line[2] not in third_digits:
#         third_digits.append(line[2])

# print(first_digits)
# print(second_digits)
# print(third_digits)
import re

combos = [319680180690129620762689762318368710720710629168160689716731736729316729729710769290719680318389162289162718729319790680890362319760316729380319728716,
319680180690129620762689762318368710720629168160689716731736729316729729710769290719680318389162289162718729319790680890362319760316729380319728716,
31968018069012962076268976231836871072062916816689716731736729316729729710769290719680318389162289162718729319790680890362319760316729380319728716,
319680180690129620762689318368710629168160716731736729719290780382282718790890362760329380726]

# Maybe flip it on it's head and instead work on the combos to reduce it to the smallest number by removing repetition of the 3 digits?
all_combined = ''.join([line for line in lines])

ix = 0
while ix < len(all_combined) - 2:
    # Attempt to remove duplication of the same 3 digits from later in the string
    all_combined = all_combined[0:ix+3] + all_combined[ix+3:].replace(all_combined[ix:ix+3], '')
    ix += 1

print(all_combined)

# This is slow but does seem to satisfy me in checking if all lines are found in sequence
for i in range(100000, 999999):
    found = 0
    for line in lines:
        sequence_found = False
        if str(i).find(line[0]) > -1:
            firsts = [m.start() for m in re.finditer(line[0], str(i))] 
            seconds = [m.start() for m in re.finditer(line[1], str(i)[firsts[0]:])] 
            if len(seconds) > 0:
                thirds = [m.start() for m in re.finditer(line[2], str(i)[seconds[0]:])]
                if len(thirds) > 0:
                    for first in firsts:
                        for second in seconds:
                            if second > first:
                                for third in thirds:
                                    if third > second:
                                        sequence_found = True
                                        found +=1
                                        break
                                
                                if sequence_found:
                                    break
                            
                            if sequence_found:
                                break
        
        if found == len(lines):
            print(i)
            break

            # if str(i).find(line[0]) > -1 and str(i).find(line[0]) < str(i).find(line[1]) and str(i).find(line[1]) < str(i).find(line[2]):
            #     found +=1
            #     print(line)
            #     print(line[0])
            #     print(line[1])
            #     print(line[2])
            #     if found == len(lines):
            #         print(i)
            #         break



# #Doing it manually
# 319
# 680
# 180
# 690

# 319 # None present so add all in order
#    680  # No matches so add all at end
# 319680
#  1  80  # Matches in order mean nothing new to add at the end
# 319680
#    6 90
# 3196890 # First match in order, third match in order, second digit needs to insert somewhere between the first and third in the sequence. 
# # WTF do I do if it can go in 2 places here? I need to generate 2 possible combinations and then keep going
# 3196890
# 3196980

# So each combination needs to fit all of the cases. Maybe I should instead start at a big number containing all of the digits and iterate to find the pattern which matches?
# I think this is along the lines of Alex's brute force description

# for i in range(11111111, 19999999):
#     found = 0
#     for line in lines:
#         if line[0] in str(i) and line[1] in str(i) and line[2] in str(i):
#             if str(i).find(line[0]) > -1 and str(i).find(line[0]) < str(i).find(line[1]) and str(i).find(line[1]) < str(i).find(line[2]):
#                 found +=1

#     if found == len(lines):
#         print(i)

# The more elegant way seems to be along the lines of finding the possible combinations as you iterate through each new number but matching where you can.
# So you have a small amount of combinations to look at then picking the smallest in length but each final number needs to satisfy all before it
# pins = []
# for line in lines:
#     pin = []
#     # Go through each number in the line
#     for digit_index, digit in enumerate(line):
#         digit_found = False
#         # Go through all digits in the pin
#         for pin_index, num in enumerate(pin):
#             # If the digit appears in the pin already ignore it
#             if digit == num:
#                 digit_found = True
        
#         # Dealing with the first unfound digit and an empty pin
#         if not digit_found:
#             if digit_index == 0 and len(pin) == 0:
#                 pin.insert(0, digit)
#             # If it is the first digit and the second is not in the pin then add this to the end
#             elif len(pin) > 0 and digit_index == 0 and line[1] not in pin:
#                 pin.append(digit)
#             # If digit is not found but the subsequent digit is found add this number in front of it
#             elif len(pin) > 0 and digit_index == 0 and line[1] in pin:
#                 pin.insert(pin.index(line[1])-1, digit)
#             # If digit is not found but the earlier digit is found add this number behind it
#             elif len(pin) > 0 and digit_index == 1 and line[0] in pin:
#                 pin.insert(pin.index(line[0])+1, digit)
#             # If digit is not found but the earlier digit is found add this number behind it
#             elif len(pin) > 0 and digit_index == 2 and line[1] in pin:
#                 pin.insert(pin.index(line[1])+1, digit)
#             else:
#                 pin.append(digit)