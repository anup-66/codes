# T = int(input())
# for _ in range(T):
    # n,m = map(int,input().split())
    # a = input()
    # dict_ = {}
    # for i in a:
    #     if i in dict_:
    #         dict_[i] +=1
    #     else:
    #         dict_[i] = 1
    # count = 0
    # for j in ["A","B","C","D","E","F","G"]:
    #     if j in dict_:
    #         if dict_[j]<m:
    #             count+=m-dict_[j]
    #     else:
    #         count+=m
    # print(count)
#
# T = int(input())
# for _ in range(T):
#     n,f,k = map(int,input().split())
#     arr = list(map(int,input().split()))
#     val = arr[f-1]
#     arr = sorted(arr,reverse = True)
#     if arr[k-1]<val:
#         print("YES")
#     elif arr[k-1]>val:
#         print("NO")
#     else:
#         if k==len(arr):
#             print("YES")
#         else:
#             if arr[k-1]==arr[k]:
#                 print("MAYBE")
#             else:
#                 print("YES")
#
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     o_arr = list(map(int,input().split()))
#     b_arr = list(map(int,input().split()))
#     m = int(input())
#     d = list(map(int,input().split()))
#     set_ = set()
#     dict_ = {}
#     for i in range(len(o_arr)):
#         if o_arr[i]!=b_arr[i]:
#             # set_.add(b_arr[i])
#             if b_arr[i] in dict_:
#                 # print(dict_)
#                 # print(b_arr[i] in dict_)
#                 dict_[b_arr[i]] += 1
#             else:
#                 dict_[b_arr[i]] = 1
#     d_dict_ = {}
#     for i in d:
#         if i in d_dict_:
#             d_dict_[i]+=1
#         else:
#             d_dict_[i] = 1
#     flag = True
#     for j in dict_:
#         if j not in d_dict_:
#             flag = False
#             break
#         if dict_[j]!=d_dict_[j]:
#             flag = False
#             break
#     if not flag:
#         print("NO")
#     else:
#         if d[-1] in b_arr:
#             print("YES")
#         else:
#             # print("rr")
#
#             print("NO")

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     # str_ = ""
#     s = input()
#     # for i in range(n):
#     str_=s[n-1]*n
#     print(str_)


# ababa
# baba
# aaba
# aba
# bba
# ba
# aa
# a
# b
# set_ = set()
def find(str_, set_):
    if not str_:
        return 0

    one = str_[1:]
    second = str_[0] + str_[2:]
    count = 0
    if one not in set_:
        set_.add(one)
        count += 1 + find(one, set_)
    if one==second:
        return 2*count
    if second not in set_:
        set_.add(second)
        count += 1 + find(second, set_)
    return count
def find1(str_, set_):
    queue = []
    count = 0
    queue.append(str_)
    dp = {}
    while queue:
        str_ = queue.pop(0)
        if not str_:
            continue
        one = str_[1:]
        second = str_[0] + str_[2:]
        if one not in set_:
            queue.append(one)
            count+=1
            set_.add(one)

        if second not in set_:
            queue.append(second)
            count+=1
            set_.add(second)
    return count
def find3(str_):
    dp = [0]*n
    dp[0] = 1
    pass

#
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    set_ = set()

    if len(s)==1:
        print(1)
    else:
        count = find(s,set_)
        print(count)
