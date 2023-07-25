# A googol (10**100) is a massive number: one followed by one-hundred zeros; 
# 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 
# .

# Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?

def sum_digits(num: int):
    num_str = str(num)
    sum_num = 0
    for digit in num_str:
        sum_num += int(digit)
    return sum_num

largest_digit_sum = 0
largest_sum_a = 0
largest_sum_b = 0
for a in range(1,100):
    for b in range(1,100):
        c = a**b
        c_sum = sum_digits(c)
        if c_sum > largest_digit_sum:
            largest_digit_sum = c_sum
            largest_sum_a = a
            largest_sum_b = b

print(f"Largest digit sum found = {largest_digit_sum} from a: {largest_sum_a} and b: {largest_sum_b}")
