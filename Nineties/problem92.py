# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

starting_num = 85

def add_square_digits(n):
    output = 0
    for i in str(n):
        output += int(i) ** 2
    return output

total = 0
num = 1
i = 1
while i < 10000000:
    num = i
    while 1 == 1:
        num = add_square_digits(num)
        if num == 1:
            break
        if num == 89:
            total += 1
            break
    i += 1
    
print(total)