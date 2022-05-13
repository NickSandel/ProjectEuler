# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Fibonacci sequence setup
a = []
a.append(1)
a.append(2)
# Because the sequence needs seeding with 1 and 2
for i in range(10):
    a.append(a[i] + a[i + 1])

print(a)

# Setup the sequence to stop when the new value will exceed 4 million
b = []
b.append(1)
b.append(2)
while b[len(b)-2] + b[len(b)-1] < 4000000:
    b.append(b[len(b)-2] + b[len(b)-1])

print(b)

# Find even terms and sum them up
c = sum([x for x in b if x % 2==0])
print(c)    