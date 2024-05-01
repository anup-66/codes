l1,r1,l2,r2 = map(int,input().split())
if l1>0 and r1>0 and l2>0 and r2>0:
    print(r1*r2)
elif l1<0 and r1>0:
    if r2>0:
        print(r1*r2)
    else:
        print(max(l1*l2,r1*l2))
elif l1>0 and r1<0:
    if r2>0:
        print(l1*r2)
    else:
        print(max(l1*l2,r1*r2))