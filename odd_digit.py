import math
count = 0
n = int(input())
for i in range(1,n+1):
    count+=1&(math.floor(math.log10(i)) + 1)

print(count)

if 1<=n<=99:
    print(9)
elif 100<=n<1000:
    print(10 + (n-100))
elif 1000<=n<10000:
    print(909)
elif 10000<=n<100000:
    print(910 + (n - 10000))
else:
    print(90909)

print(2 + 3 - 25/2*5)