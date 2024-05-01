alph = "".join([chr(i) for i in range(97,123)])
str_ = input()
for i in alph:
    if i in str_:
        continue
    else:
        print(i)
        break
