def breakIt(s,i,j,res):
    if j>=len(s):
        res.append(s[i:j+1])
        return res
    if s[j]!="#":
        return breakIt(s,i,j+1,res)
    else:
        res.append(s[i:j])
        while j<len(s) and s[j]=="#":
            j+=1

        return breakIt(s,j,j,res)

res = breakIt("122345678#",0,0,[])
print([i for i in res if i!=""])