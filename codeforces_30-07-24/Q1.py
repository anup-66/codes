# N = int(input())
# for _ in range(N):
#     str_ = input()
#     if len(str_)==1:
#         val = str_
#         if val=="z":
#             val = "a"
#         else:
#             val = chr((ord(str_) + 1))
#         print(val+str_)
#     else:
#         prev = str_[0]
#         new_str = prev
#         flag = True
#         for i in range(1,len(str_)):
#             # print(str_[i],prev)
#             if str_[i]==prev and flag:
#                 # print("uhuhhuhu")
#                 val = str_[i]
#                 if val=="z":
#                     val = "a"
#                 else:
#                     val = chr(ord(str_[i])+1)
#                 new_str+=val
#                 flag = False
#             new_str+=str_[i]
#             prev = str_[i]
#         if len(new_str)==len(str_)+1:
#             print(new_str)
#         else:
#             val = new_str[-1]
#             if val=="z":
#                 val = "a"
#             else:
#                 val = chr(ord(new_str[-1]) + 1)
#             print(new_str+val)
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     mat = []
#     for j in range(2):
#         mat.append([i for i in input()])
#     count = 0
#     for i in range(1, N-1):
#         if mat[0][i]=="." and mat[1][i-1]=="x" and mat[1][i+1]=="x" and mat[0][i-1]=="." and mat[0][i+1]=="." and mat[1][i]==".":
#             count+=1
#     for i in range(1, N - 1):
#         if mat[1][i] == "." and mat[0][i - 1] == "x" and mat[0][i + 1] == "x" and mat[1][i-1]=="." and mat[1][i+1]=="." and mat[0][i]==".":
#             count += 1
#     print(count)

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     str_ = input()
#     stack = []
#     stack.append(("(",1))
#     ans = 0
#     for i in range(1,len(str_)):
#         if str_[i]==")":
#             if stack:
#                 res = i+1 - stack[-1][1]
#                 stack.pop()
#                 ans+=res
#         if str_[i]=="(":
#             stack.append(("(",i+1))
#         if str_[i]=="_":
#             if stack:
#                 res = i+1-stack[-1][1]
#                 ans+=res
#                 stack.pop()
#             else:
#                 stack.append(("(",i+1))
#     print(ans)

T = int(input())
for _ in range(T):
    N = int(input())
    vertices  = [0,1,2,3,4,5,6,7]
    # p = list(map(int,input().split()))
    dict_ = {0:[2,3],2:[1],1:[4],4:[],3:[5,6],5:[7],6:[]}
    root = 0
    def find(node):
        if node not in  dict_:
            return vertices[node]
        res1 = find(dict_[node][0])
        if len(dict_[node])==2:
            res2 = find(dict_[node][1])
        else:
            res2 = float("inf")
        return (min(res1,res2) + vertices[node])//2
    left = find(dict_[root][0])
    if len(dict_[root])==2:
        right = find(dict_[root][1])
    else:
        right = float("inf")
    print(min(left,right))


