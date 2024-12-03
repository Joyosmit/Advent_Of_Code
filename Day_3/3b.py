fh = open("input.txt","r")
lines = fh.readlines()
ans = 0
from typing import Tuple

def check(line:str) -> Tuple[int, bool]:
    ans = True
    print(line)
    if line[0]!="(":

        ans = False
        return (-1,ans)
    num1 = ''
    for ch in line[1:]:
        if ch!=",":
            if not ch.isdigit():
                return (-1, False)
            num1+=ch
        else:
            break
    comma_ind = line.find(",")
    num2 = ''
    for ch in line[comma_ind+1:]:
        if not ch.isdigit():
            break
        num2+=ch
    if line[comma_ind+1+len(num2)]!=")":
        return (-1,False)
    if len(num1)>3 or len(num2)>3:
        return (-1, False)
    num1 = int(num1)
    num2 = int(num2)
    return (num1*num2, True)

start = True
for line in lines:
    n = len(line)
    for i in range(n-2):
        if line[i:i+4]=="do()":
            start = True
        elif line[i:i+7]=="don't()":
            start = False
        if line[i:i+3] == "mul" and start:
            (val, b)=check(line[i+3:i+12])
            if b:
                ans+=val
print(ans)