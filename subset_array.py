# def subset(start,end,arr):
#     if end>len(arr)-1:
#         return
#     print(arr[start:end])
#     subset(start,end+1,arr)
#
arr = [1,2,3,4,5,6,7,9,10]
# for i in range(len(arr)):
#     subset(i,i+1,arr)


def subset(res,index,s,arr):
    res.append(s[:])
    for i in range(index,len(arr)):
        s.append(arr[i])
        subset(res,i+1,s,arr)
        s.pop()

for _ in range(int(input())):
    res = []
    arr = list(map(int,input().split()))
    val = subset(res,0,[],arr)
    print(len(res))
