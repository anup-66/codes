def find(s1,s2,i1,i2,num,target):
    print(i1,i2)
    if num==target:
        return True
    if i1==len(s1)-1:
        return False
    if s1[i1]==s2[i2]:
        if find(s1,s2,i1+1,i2+1,num+1,target):
            return True
    else:
        if find(s1,s2,i1+1,0,0,target):
            return True
    return False
s1 = input()
s2 = input()
target = len(s2)
if find(s1,s2,0,0,0,target):
    print("yes")
else:
    print("NO")