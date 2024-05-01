avg = 0
str_ = input()
for i in str_:
    avg+=ord(i)
val = avg/len(str_)
print("%.2f " % val)