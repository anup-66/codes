arr = list(map(int,input().split()))
if arr[-1]==0:
    print(-1)
else:
    l =0
    r = len(arr)-1
    flag = False
    while l<=r:
        mid = l + (r - l)//2
        if arr[mid]==1 and arr[mid-1]==0:
            print(mid)
            flag = True
            break
        if arr[mid]==1:
            r = mid-1
        else:
            l = mid+1
    if not flag:
        print(-1)