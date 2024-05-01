val = int(input())


def find(val):
    str_ = ""
    neg = False
    if val<0:
        neg = True
        val = -val

    while val > 0:
        if val % 2 == 0:
            str_ += "0"
        else:
            str_ += "1"
        val = val // 2
    if neg:
        nstr_ = ""
        for i in range(len(str_)):
            if str_[i]=="0":
                nstr_+="1"
            else:
                nstr_+="0"
        # nstr_+="1"
        carry = 1
        newstr_ = ""
        for i in nstr_:
            if i=="1":
                if carry==1:
                    newstr_+="0"
                    carry = 1
                else:
                    newstr_+="1"
                    carry = 0
            else:
                if carry==1:
                    newstr_+="1"
                    carry = 0
                else:
                    newstr_+="0"
                    carry = 0

        return newstr_+"1"
    return str_


print(find(val)[::-1])
