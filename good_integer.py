import math

a = list(map(int,input().split()))
n = len(a)
numbers = [i for i in range(1,int(math.pow(max(a),1/3)))]
count = 0
for i in range(len(a)):
    # print(i)
    for j in [v for v in range(1,int(math.pow(a[i],1/3)) + 1)]:
        res = a[i] - j**3
        # print(a[i],j**3,res)
        if res>0 and math.pow(res,1/3)==int(math.pow(res,1/3)):
            count+=1
            break



print(count)