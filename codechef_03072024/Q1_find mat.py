T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    if m==1 and n==1:
        print(-1)
        continue
    if m>1:
        for i in range(n):
            for j in range(m-1):
                mat[i][j],mat[i][j+1] = mat[i][j+1],mat[i][j]
    else:
        for i in range(n-1):
            mat[i][0],mat[i+1][0] = mat[i+1][0],mat[i][0]

    for i in range(n):
        for j in range(m):
            print(mat[i][j],end = " ")
        print()

