from math import fabs
fh = open("input.txt", "r")
lines = fh.readlines()
ans = 0
def check(l1):
    if (l1!=sorted(l1) and l1!=sorted(l1, reverse=True)):
        print(f"Here {l1}")
        return False
    for i in range(len(l1)-1):
        if not(1<= fabs(l1[i]-l1[i+1]) <= 3):
            return False
    return True
for line in lines:
    l1 = list(map(int, line.split(" ")))
    emp = []
    if check(l1):
        print(f"Good Line is {l1} and emp is {emp}")
        ans+=1
        continue
    for i in range(len(l1)):
        emp[:] = l1[:i]+l1[i+1:]
        print(f"Line is {l1} and emp is {emp}")
        if check(emp):
            print(f"Good Line printed is {l1} and emp is {emp}")
            ans+=1
            break
    # else:
    #     ans+=1
    # print(line.split(" "))
print(ans)
        