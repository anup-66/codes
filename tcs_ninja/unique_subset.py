s = input()
set_ =[False]*26
l = 0
max_len = -1
for i in range(len(s)):
    if ord(s[i])==False:
        set_[ord(s[i])] = True
    else:
        while s[i] in set_:
            set_.remove(s[l])
            l+=1
        set_.add(s[i])
    max_len = max(i-l+1,max_len)
print(max_len)