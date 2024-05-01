array = [2,0,1,2,4,5]
narr = []
dict_ = set()
for i in array:
    if i in dict_:
        continue
    else:
        dict_.add(i)
        narr.append(i)
print(narr)

# [0,0,0,0,1,0,1,0,2,0,1,0,2,0,2]