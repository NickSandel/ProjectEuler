first = 1
last = 100
sumsquare = 0
sumrange = 0
for i in range(first,last + 1):
    sumsquare += i * i
    sumrange += i

print(sumsquare)
print(sumrange)

print((sumrange * sumrange) - sumsquare)

# From the docs
# Sum of a range can be simplified to sum(n) = n(n+1)/2
sumrange = last*(last+1)/2
print(sumrange)
sumsquare = (2*last+1)*(last+1)*last/6
print(sumsquare)
print((sumrange * sumrange) - sumsquare)