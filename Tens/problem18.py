# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

#               75
#              95 64
#             17 47 82
#            18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

# I wonder if this is about looking at future options maybe as little as 2 options ahead. 
# So if you pick one number pick the biggest off of that and then compare it to the other possible routes from where you are
# I think this has to be a top down approach

# little_array = [
#     [3],
#     [7,4],
#     [2,4,6],
#     [8,5,9,3]
#     ]

# #First thing is to align the walker. I think this is fairly simple because where you are will only be slightly offset from where you can go. 
# # E.g. if you're at index 0 you can go to 0/1. At 1 you can go to 1/2
# current_index = 0
# sum_values = 0
# for index, row in enumerate(little_array):
#     sum_values += row[current_index]
#     # Unless you're on the last row pick the next index
#     if index+1 < len(little_array):
#         left_val = little_array[index + 1][current_index]
#         right_val = little_array[index + 1][current_index + 1]
#         if left_val < right_val:
#             current_index = current_index + 1
#         print(little_array[index + 1][current_index])

# print(sum_values)

big_array = [
              [75],
             [95, 64],
            [17, 47, 82],
           [18, 35, 87, 10],
          [20, 4, 82, 47, 65],
         [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
       [99, 65, 4, 28, 6, 16, 70, 92],
      [41, 41, 26, 56, 83, 40, 80, 70, 33],
     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
   [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
 [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]

# print('--------------------')

# current_index = 0
# sum_values = 0
# print(big_array[0][0])
# for index, row in enumerate(big_array):
#     sum_values += int(row[current_index])
#     # Unless you're on the last row pick the next index
#     if index+1 < len(big_array):
#         left_val_next = int(big_array[index + 1][current_index])
#         right_val_next = int(big_array[index + 1][current_index + 1])

#         # If there is another row check the values possible to see if left or right yield a bigger number
#         if index+2 < len(big_array):
#             # On the next next row there will be 3 options, left, middle and right. If middle is the best then it will be shared so pick the larger of left or right
#             left_val_next_next = max(big_array[index + 2][current_index], big_array[index + 2][current_index+1])

#             if current_index + 2 == len(big_array[index+2])-1:
#                 right_val_next_next = max(big_array[index + 2][current_index + 1],big_array[index + 2][current_index + 2])
#             else:
#                 right_val_next_next = max(big_array[index + 2][current_index], big_array[index + 2][current_index + 1])
#         else:
#             left_val_next_next = 0
#             right_val_next_next = 0

#         left_val = left_val_next + left_val_next_next
#         right_val = right_val_next + right_val_next_next
#         if left_val < right_val:
#             current_index = current_index + 1
#         print(int(big_array[index + 1][current_index]))

# print(sum_values)

# #Huh I found a slightly more optimal route than just going next biggest, got to 1068 instead of 1064

# #Maybe try another fairly simple approach of flip it on it's head and start from the largest value(s) and see how you can walk back up the pyramid?
# current_index = 7#big_array[len(big_array) - 1].index(max(big_array[len(big_array) - 1]))
# for row_num in range(len(big_array) - 1, 0, -1):
#     print(big_array[row_num][current_index])
#     sum_values += big_array[row_num][current_index]

#     # Unless you're on the last row pick the next index
#     if row_num-1 > 1:
#         left_val = big_array[row_num-1][current_index-1]

#         # If right val is on the end you must go left
#         if len(big_array[row_num-1]) == current_index + 1:
#             right_val = 0
#         else:
#             right_val = big_array[row_num-1][current_index]

#         if left_val > right_val:
#             current_index = current_index - 1

# print(sum_values)

# Still wrong but got a much bigger number. There are 2 98's in the bottom of the pyramid though, perhaps I need to force it to try the other one. 
# No that one gets to 1978 which is lower

# There is clearly some smart trick I'm completely missing here...
# Alex helped nudge me in the right direction. Don't try and follow a single path instead start at the bottom and follow them all simultaneously... add up as you go!

new_array=big_array.copy()
for row_num in range(len(big_array) - 2, -1, -1):
    print(new_array[row_num])
    for row_index in range(len(new_array[row_num])):
        row_left = new_array[row_num+1][row_index]
        row_right = new_array[row_num+1][row_index+1]

        new_array[row_num][row_index] = new_array[row_num][row_index] + max(row_left, row_right)

print(new_array)