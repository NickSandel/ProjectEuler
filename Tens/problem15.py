# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many in a 3x3 grid? 20 (manually worked out I think) How many in a 4x4 grid?

# How many such routes are there through a 20×20 grid?

# Oops I cheated and figured it out using this article: https://www.xarg.org/puzzle/project-euler/problem-15/

def countroutes(x,y):
    if x == 0 or y == 0:
        return 1
    else:
        return countroutes(x, y-1) + countroutes(x-1, y)

print(countroutes(2,2))
print(countroutes(3,3))
print(countroutes(20,20))