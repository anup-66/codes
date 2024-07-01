arr = list(map(int,input().split()))
dict_ = {i:0 for i in arr}
for i in arr:
    dict_[i] +=1

for i in arr:
    if dict_[i]==1:
        print(i)
        break
