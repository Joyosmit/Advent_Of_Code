from math import fabs
fh = open("2_inp.txt", "r")
lines = fh.readlines()
ans = 0
for line in lines:
    l1 = list(map(int, line.split(" ")))
    
    if (l1!=sorted(l1) and l1!=sorted(l1, reverse=True)):
        continue
    for i in range(len(l1)-1):
        if not(1<= fabs(l1[i]-l1[i+1]) <= 3):
            break
    else:
        ans+=1
    # print(line.split(" "))
print(ans)
        