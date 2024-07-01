arr = list(map(int,input().split()))
K = int(input())
max_ = -1
for i in range(len(arr)):
    temp = 0
    for k in range(K):
        if i+k>len(arr)-1:
            continue
        temp+=arr[i+k]
    if max_<temp:
        max_ = temp
        # temp = 0
# print(max_)
max_ = sum(arr[:3])
g_max = max_
l = 0
for i in range(3,len(arr)):
    new_ = max_ + arr[i] - arr[l]
    l+=1
    if new_>g_max:
        # max_ = new_
        g_max = new_
    max_ = new_
print(max_)