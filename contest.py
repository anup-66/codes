# # T = int(input())
# # for _ in range(T):
# #     n= int(input())
# #     arr = list(map(int,input().split()))
# #     evp = [0]*(n+2)
# #     oddp = [0]*(n+2)
# #     evs = [0]*(n+2)
# #     odds = [0]*(n+2)
# #     evp[1] = arr[0]
# #     oddp[1] = arr[1]
# #     for i in range(1,len(arr)+1):
# #         if (i-1)%2==0:
# #             evp[i] = evp[i-1] + arr[i-1]
# #             oddp[i] = oddp[i-1]
# #         else:
# #             evp[i] = evp[i-1]
# #             oddp[i] = oddp[i - 1] + arr[i-1]
# #
# #     for i in range(n,0,-1):
# #         if i%2==0:
# #             evs[i] = evs[i + 1] + arr[i-1]
# #             odds[i] = odds[i+1]
# #         else:
# #             evs[i] = evs[i+1]
# #             odds[i] = odds[i + 1] + arr[i-1]
# #     print(evp)
# #     print(oddp)
# #     print(odds)
# #     print(evs)
# #     for i in range(len(arr)):
# #         if i%2==0:
# #             sum_even = evp[i] + odds[i+2]
# #             sum_odd = oddp[i] + evs[i+2]
# #             # print(sum_even,sum_odd)
# #             if sum_even==sum_odd:
# #                 print(i)
# #         else:
# #             sum_even = evp[i ] + evs[i + 2]
# #             sum_odd = oddp[i] + odds[i + 2]
# #             if sum_even==sum_odd:
# #                 print(i)
#
# from collections import Counter
#
# str1 = input()
# set_ = set()
# for i in str1:
#     if 65<=ord(i)<=90 or 97<=ord(i)<=122:
#         set_.add(i)
#
# if len(set_)==26:
#     print(True)
# else:
#     print(False)
#
#
#
# from collections import deque
# T = int(input())
# for _ in range(T):
#     N,Q,D = map(int,input().split())
#     res = deque()
#     res.append(D-1)
#     for i in range(Q):
#         a, b = input().split()
#         a = int(a)
#         if b=="?":
#             lr = len(res)
#             for i in range(lr):
#                 vale = res.popleft()
#                 newa = (vale + a) % N
#                 newb = (vale - a) % N
#                 res.append(newa)
#                 res.append(newb)
#         elif b=="0":
#             lr = len(res)
#             for i in range(lr):
#                 vale = res.popleft()
#                 newa = (vale + int(a)) % N
#                 res.append(newa)
#         else:
#             lr = len(res)
#             for i in range(lr):
#                 vale = res.popleft()
#                 newa = (vale - int(a)) % N
#                 res.append(newa)
#
#     s = sorted(set(res))
#     print(len(s))
#     for i in s:
#         print(i+1,end=" ")
#     print()


T = int(input())

for _ in range(T):
    N, Q, D = map(int, input().split())
    dp = [0] * N
    dp[(D - 1) % N] += 1
    for i in range(Q):
        a, b = input().split()
        a = int(a)
        if b == "?":
            new_dp = [0] * N
            for j in range(N):
                new_dp[(j + a) % N] += dp[j]
                new_dp[(j - a) % N] += dp[j]
            dp = new_dp
        elif b == "0":
            new_dp = [0] * N
            for j in range(N):
                new_dp[(j + a) % N] += dp[j]
            dp = new_dp
        else:
            new_dp = [0] * N
            for j in range(N):
                new_dp[(j - a) % N] += dp[j]
            dp = new_dp

    count = sum(1 for x in dp if x > 0)
    print(count)
    for i in range(N):
        if dp[i] > 0:
            print(i + 1, end=" ")
    print()



