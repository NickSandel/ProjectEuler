# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
# [
#     [131 673 234 103 18],
#     [201 96 342 965 150],
#     [630 803 746 422 111],
#     [537 699 497 121 956],
#     [805 732 524 37 331]
# ]
 
# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), 
# a 31K text file containing an 80 by 80 matrix.


# Ok maybe this is a bit similar to the tree navigation. There are different directions involved and different dimensions to navigate but still a start and a finish
# Let's play with the mini matrix first

sample = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]

def map_path_right_down(matrix_array):
    # Start in the bottom left and apply the addition back up the tree?
    for row in range(len(matrix_array)-1, -1, -1):
        for column in range(len(matrix_array[row])-1, -1, -1):
            if row == len(matrix_array)-1 and column == len(matrix_array[row])-1:
                continue
            # From bottom right paths into it are left and up so pick smallest and add previous value to it
            # If you're on the end you can only look down
            elif column == len(matrix_array[row])-1:
                matrix_array[row][column] = matrix_array[row][column] + matrix_array[row+1][column]
            # If you're on the bottom row you can only look right
            elif row == len(matrix_array)-1:
                matrix_array[row][column] = matrix_array[row][column] + matrix_array[row][column+1]
            # Otherwise pick the smallest value!
            else:
                matrix_array[row][column] = matrix_array[row][column] + min(matrix_array[row+1][column], matrix_array[row][column+1])

    return matrix_array

# print(map_path_right_down(sample))

p81_matrix = []
with open('p081_matrix.txt', 'r') as f:
    for line in f.readlines():
        line = line.split(',')
        row = []
        for value in line:
            value = value.replace('\n', '')
            intvalue = int(value)
            row.append(intvalue)
        p81_matrix.append(row)

summed_matrix = map_path_right_down(p81_matrix)
print(summed_matrix[0][0])