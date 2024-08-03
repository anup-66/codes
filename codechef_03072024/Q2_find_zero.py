# T = int(input())
# for _ in range(T):
#     n,k = map(int,input().split())
#     arr = list(map(int,input().split()))
#     dp = [0]*(len(arr)+1)
#     ans = 0
#     for i in arr:
#         if i<k:
#             ans+=1
#     if arr[0]<k:
#         dp[0] = arr[0]
#         ans+=1
#     else:
#         ans-=1
#         dp[0] = 0
#     for i in range(len(arr)):
#         val1 = dp[i-1] + arr[i]
#         val2 = arr[i-1] + arr[i]
#         if val1<k:
#             ans+=1
#             dp[i] = val1
#         else:
#             dp[i] = 0
#         if val2<k:
#             ans+=1
#         else:
#             dp[i] = 0
#     print(ans)
#
# # dp[i-1] + arr[i]
# # arr[i-1] + arr[i]
# #
# # 1 2 3,0 1
import pywhatkit

pywhatkit.sendwhatmsg("+917970954003",
                      "Geeks For Geeks!",
                      16, 8)