
# def hcfnaive(a, b):
#     if(b == 0):
#         return abs(a)
#     else:
#         return hcfnaive(b, a % b)
#
# print(hcfnaive(1000,999))
# T = int(input())
# for _ in range(T):
#     num = int(input())
#     max_ = -1
#     for i in range(1,num):
#         if num%i==0:
#             max_ = i
#             break
#     print(num - max_)


# T = int(input())
# for _ in range(T):
#     n,m = map(int,input().split())
#     a = input()
#     b = input()
#     if a==b:
#         print(len(a))
#     else:
#         i = 0
#         j = 0
#         count = 0
#         while i<len(a) and j<len(b):
#             if a[i]==b[j]:
#                 count+=1
#                 i+=1
#                 j+=1
#             else:
#                 j+=1
#         print(count)

""""c"""
from functools import cache

# T = int(input())
# for _ in range(T):
#     size =int(input())
#     arr = list(map(int,input().split()))
#     res = [10**9]
#     for i in range(size-2,-1,-1):
#         res.append(res[-1] - arr[i])
#     print(*res[::-1])
#

# T = int(input())
# for _ in range(T):
#     n,k,b,s = map(int,input().split())
#     p = list(map(int,input().split()))
#     a = list(map(int,input().split()))
#
#     # @cache
#     def find(sum_,index,c):
#         if c>=k:
#             return sum_
#         val1 = find(sum_ + a[index],p[index]-1,c+1)
#         val2 = find(sum_+a[index],index,c+1)
#         return max(val1,val2)
#
#     bb = find(0,b-1,0)
#     ss = find(0,s-1,0)
#
#     if bb>ss:
#         print("Bodya")
#     elif bb<ss:
#         print("Sasha")
#     else:
#         print("Draw")


from collections import defaultdict
T = int(input())
for _ in range(T):
    n,k,q = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    a = [0]
    b = [0]
    for i in range(len(arr)):
        a.append(arr[i])
        b.append(brr[i])
    dict_ = [0]*(k+1)
    # dict_.append(0.0)
    j = 1
    for i in range(1,k+1):
        if i<=a[j]:
            speed =((a[j] - a[j-1])/(b[j] - b[j-1]))
            dict_[i] = dict_[i-1] + float(1/speed)
        else:
            j+=1
            speed = ((a[j] - a[j - 1]) / (b[j] - b[j - 1]))
            dict_[i] = dict_[i - 1] + float(1 / speed)
    print(dict_)
    for k in range(q):
        print(int(dict_[int(input())]),end = " ")
    print()

