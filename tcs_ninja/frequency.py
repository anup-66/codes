s = input()
if not s:
    print("")
dict_ = {i:0 for i in s if 97<=ord(i)<=122}
# for i in s:
#     print(ord(i))
#     if 97<=ord(i)<=122:
#         print(i)
max_ = 0
for i in s:
    dict_[i]+=1
    max_ = max(max_,dict_[i])
# print(dict_)
# print(max_)
res = max_
ans = []
for i in dict_:
    if dict_[i]==res:
        ans.append(i)
# print(ans)
print(sorted([ans])[-1])