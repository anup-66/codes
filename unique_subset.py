

def subset(res,index,s,arr,a):
    s.add(tuple(a[:]))
    for i in range(index,len(arr)):
        a.append(arr[i])
        subset(res,i+1,s,arr,a)
        a.pop()
    return s

for _ in range(int(input())):
    res = []
    set_ = set()
    arr = list(map(int,input().split()))
    val = subset(res,0,set_,arr,[])
    print(val)
