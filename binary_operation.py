s = input()

res = int(s[0])
for i in range(1,len(s)-1,2):
    if s[i]=="A":
        res = res & int(s[i+1])
    elif s[i]=="B":
        res = res | int(s[i+1])
    else:
        res = res ^ int(s[i+1])

print(res)


stack = []

stack.append(int(s[0]))

for i in range(1,len(s)):
    if i=="A":
        stack.append(stack.pop() & int(s[i+1]))
    elif i=="B":
        stack.append(stack.pop() | int(s[i + 1]))
    elif i=="C":
        stack.append(stack.pop() ^ int(s[i + 1]))
print(*stack)