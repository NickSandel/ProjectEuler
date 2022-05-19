import numbers
oddNumbers = [1,3,5,7,9]
evenNumbers = [0,2,4,6,8]

numberRange = 20
divisorList = []
primes = []

for i in range (numberRange):
    lastdigit = int(repr(i)[-1])
    if lastdigit in oddNumbers and i > 1 and i < numberRange/2:
        divisorList.append(i)
		
#print (divisorList)

for n in range (numberRange):
    lastdigit = int(repr(n)[-1])
    if lastdigit not in evenNumbers and lastdigit != 5:
        #print (n, ' is even')
    #else:
        for u in divisorList:
            #result = n/u
            remainder = n % u
            #if result.is_integer() and result > 1:
            #print (n, ' divided by ', u, ' is whole ', result)
            if remainder == 0 and n != u:
                #print (n, ' divided by ', u, ' is whole ', remainder)
                break
            else:
                if u is divisorList[-1]:
                    primes.append(n)
                    print(n)
    if n == 5: #The last digit logic removes 5
        primes.append(n)
		
print(len(primes))
print(sorted(primes))