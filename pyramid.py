n = int(input())
res = 3
ans = 0
for i in range(1,n+1):
    ans+=(i*3)%(10e7)

ans-=(n)
print(int(ans))
# n =
print(int((n/2)*(3 + 3*n) - n))