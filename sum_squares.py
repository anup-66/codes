import math

n = int(input())

dp = [float("inf")]*(n+1)

squares = [i**2 for i in range(1,int(math.sqrt(n))+1)]
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    for j in squares:
        print(i,j)
        if i==j:
            dp[i] = 1
        elif i>j:
            dp[i] = min(dp[i],dp[i-j] + dp[j])

print(dp[-1])
