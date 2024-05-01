# # from collections import Counter
# # T = int(input())
# # for _ in range(T):
# #     N,K = map(int,input().split())
# #     arr = list(map(int,input().split()))
# #     dict_ = Counter(arr)
# #     max_ = max(dict_.values())
# #     if max_==1:
# #         print(N)
# #         continue
# #     else:
# #         if K>max_:
# #             print(N)
# #         else:
# #             print(K-1)
#
# #
# # T = int(input())
# # for _ in range(T):
# #     Row,Col = map(int,input().split())
# #     mat = []
# #     for r in range(Row):
# #         mat.append([val for val in input()])
# #     # print(mat)
# #     count_W = 0
# #     count_B = 0
# #     W = False
# #     B = False
# #     for i in mat[0]:
# #         # print(i)
# #         if i=="W":
# #             W = True
# #         if i=="B":
# #             B = True
# #     if W:
# #         count_W+=1
# #     if B:
# #         count_B+=1
# #     W = False
# #     B = False
# #     # print(count_W, count_B)
# #     for i in mat[Row-1]:
# #         if i=="W":
# #             W = True
# #         if i=="B":
# #             B = True
# #     if W:
# #         count_W+=1
# #     if B:
# #         count_B+=1
# #     W = False
# #     B = False
# #     # print(count_W, count_B)
# #     for i in mat:
# #         if i[0] == "W":
# #             W = True
# #         if i[0] == "B":
# #             B = True
# #     if W:
# #         count_W+=1
# #     if B:
# #         count_B+=1
# #     W = False
# #     B = False
# #     # print(count_W, count_B)
# #     for i in mat:
# #         if i[Col - 1] == "W":
# #             W = True
# #         if i[Col-1] == "B":
# #             B = True
# #     if W:
# #         count_W+=1
# #     if B:
# #         count_B+=1
# #     # print(count_W,count_B)
# #     if count_W == 4 or count_B==4:
# #         print("YES")
# #     else:
# #         print("NO")
#
#
# # import heapq
# # T = int(input())
# #
# # for _ in range(T):
# #     N = int(input())
# #     arr = set(list(map(int,input().split())))
# #     arr = [i for i in arr]
# #     sum_ = 0
# #     heapq.heapify(arr)
# #     alice = True
# #     bob = False
# #     while len(arr)!=1:
# #         val = heapq.heappop(arr)
# #         # print(val)
# #         if (val-sum_)==1:
# #             if bob:
# #                 alice = True
# #                 bob = False
# #             else:
# #                 alice = False
# #                 bob = True
# #             sum_+=1
# #             continue
# #         sum_+= val - 1
# #
# #     if alice:
# #         print("Alice")
# #     else:
# #         print("Bob")
# """binary string shift"""
# # T = int(input())
# # for _ in range(T):
# #     str_ = input()
# #     count = 0
# #     flag = False
# #     start = 0
# #     for i in range(len(str_)):
# #         if str_[i]=="1":
# #             flag = True
# #             start+=1
# #         if flag and str_[i]=="0":
# #             count+=start + 1
# #     print(count)
#
#
# # T = int(input())
# # for _ in range(T):
# #     n,k  = map(int,input().split())
# #     arr = list(map(int,input().split()))
# #     arr_new = sorted(arr,reverse = True)
# #     set_ = []
# #     count = 0
# #     for i in arr_new:
# #         set_.append(i)
# #         count+=1
# #         if count==k:
# #             break
# #     for val in set_:
# #         for i in range(n):
# #             if arr[i]==val and k>0 and i+1<n:
# #                 # print("i",i)
# #                 if i==0:
# #                     # print(i,arr)
# #                     arr[i] = arr[i+1] if arr[i+1]<arr[i] else arr[i]
# #                 elif i==n-1:
# #                     arr[i] = arr[i-1] if arr[i-1]<arr[i] else arr[i]
# #                 else:
# #                     arr[i] = min(arr[i-1],arr[i+1])
# #                 k-=1
# #     print(arr)
# #     print(sum(arr))
#
#
# T = int(input())
# for _ in range(T):
#     n,k = map(int,input().split())
#     a = list(map(int,input().split()))
#     b= list(map(int,input().split()))
#     arr = zip(a,b)
#     arr = sorted(arr,key = lambda x:(x[1] - x[0]),reverse = True)
#     alice = []
#     for i in range(k+1):
#         alice.append(arr[i])
#     bob = sum([val[1] for val in alice])
#     co = k
#     print(alice)
#     print(bob)
#     min_ =
#     max_ = float("inf")
#
#     for i in alice:
#         bob -= i[1]
#         co -= 1
#         if co == 0:
#             break
#     for i in arr[k:]:
#
#
#     print(bob - sum([val[0] for val in alice]))



#
# T = int(input())
# for _ in range(T):
#     size = int(input())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     j = 0
#     i = 0
#     count = 0
#     while i<len(a) and j<len(b):
#         if a[i]<=b[j]:
#             i+=1
#             j+=1
#         elif a[i]>b[j]:
#             j+=1
#             count+=1
#         # else:
#         #     i+=1
#         #     j+=1
#         # print(i,j,count)
#     print(count)


dict_ = {"U":"D","D":"U","alice":"bob","bob":"alice"}
T = int(input())
for _ in range(T):
    size = int(input())
    str_ = input()
    curr = "alice"
    u_pos = 0
    win = False
    # flag = False
    # while size>2:
    #     flag = False
    #     print(str_)
    #     for i in range(size):
    #         if str_[i]=="U":
    #             u_pos = i
    #             if str_[(i-1)%size]=="U" and str_[(i+1)%size]=="U":
    #                 print("huhhuhuu")
    #                 if i-1==0:
    #                     bef = ""
    #                 else:
    #                     bef = str_[:i-1]
    #                 str_ = bef  + dict_[str_[(u_pos-1)%size]] + dict_[str_[(u_pos+1)%size]] + str_[i+2:]
    #                 size-=1
    #                 curr = dict_[curr]
    #                 flag = True
    #                 break
    #     if not flag and str_[u_pos]=="U":
    #         print("here",u_pos,str_[:(u_pos-1)%size],str_[u_pos+2:])
    #         str_ = str_[:(u_pos-1)%size] + dict_[str_[(u_pos-1)%size]] + dict_[str_[(u_pos+1)%size]] + str_[u_pos + 2:]
    #         print(str_)
    #         size -= 1
    #         curr = dict_[curr]
    #     elif str_.count("U")==0:
    #         if dict_[curr] == "alice":
    #             print("YES")
    #         else:
    #             print("NO")
    #         win = True
    #         break
    # if not win:
    #     if str_.count("U")==0:
    #         if dict_[curr]=="alice":
    #             print("YES")
    #         else:
    #             print("NO")
    #     elif str_.count("U")==1:
    #         if curr=="bob":
    #             print("NO")
    #         else:
    #             print("YES")
    #     else:
    #         print("NO")
    count = str_.count("U")
    i = 0
    while size>2:
        if str_[i]=="U":
            u_pos = i
            if str_[(i-1)%size]=="D":
                count+=1
            if str_[(i+1)%size]=="D":
                count+=1
            if i - 1 <= 0:
                bef = ""
            else:
                bef = str_[:i-1]
            print(bef)
            str_ = bef + dict_[str_[(i - 1) % size]] + dict_[str_[(i + 1) % size]] + str_[i + 2:]
            size-=1
            i+=1
    print(str_)
    print("No" if (count/2)%2==0 else "YES")


