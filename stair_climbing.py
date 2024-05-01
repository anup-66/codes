n = int(input())
# dp = [0]*(n+1)
# dp[0] = 1
# dp[1] = 1
# for i in range(2,n+1):
#     dp[i] = dp[i-1] + dp[i-2]
#
# print(dp[-1])


def find(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return find(n-1) + find(n-2)

print(find(n))