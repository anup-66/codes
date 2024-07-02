arr = list(map(int,input().split()))
max_ = -float("inf")
res = 0
for i in range(len(arr)):
    if arr[i]>max_:
        res+=1
    max_ = max(arr[i],max_)
print(res)
