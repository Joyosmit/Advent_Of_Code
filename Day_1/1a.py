from math import fabs
fh = open("1a_inp.txt","r")
lines = fh.readlines()
ans = 0
arr1 = []
arr2 = []
for line in lines:
    l = line.split()
    arr1.append(int(l[0]))
    arr2.append(int(l[1]))
arr1.sort()
arr2.sort()
for i in range(len(arr1)):
    ans += fabs(arr1[i]-arr2[i])
print(ans)
fh.close()