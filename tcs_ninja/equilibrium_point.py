arr = list(map(int,input().split()))
n = len(arr)
pref = [0]*(n+1)
suff = [0]*(n+1)
# pref[0] = 0
for i in range(1,n):
    pref[i] = arr[i-1] + pref[i-1]
print(pref)
for i in range(len(arr)-1,0,-1):
    suff[i] = suff[i+1]  + arr[i]
print(suff)
flag = True
for i in range(n-1):
    if pref[i]==suff[i+1]:
        print(arr[i])
        flag =False
if flag:
    print(-1)