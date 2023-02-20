# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! 
# If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

big_array=[]
with open('p067_triangle.txt', 'r') as f:
    for line in f.readlines():
        line = line.split(' ')
        row = []
        for value in line:
            value = value.replace('\n', '')
            intvalue = int(value)
            row.append(intvalue)
        big_array.append(row)

print(big_array)

new_array=big_array.copy()
for row_num in range(len(big_array) - 2, -1, -1):
    print(new_array[row_num])
    for row_index in range(len(new_array[row_num])):
        row_left = new_array[row_num+1][row_index]
        row_right = new_array[row_num+1][row_index+1]

        new_array[row_num][row_index] = new_array[row_num][row_index] + max(row_left, row_right)

print(new_array)