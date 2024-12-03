from math import fabs
from collections import defaultdict
fh = open("1a_inp.txt","r")
lines = fh.readlines()
ans = 0
arr1 = []
arr2 = []
dd1 = defaultdict(lambda : 0)
for line in lines:
    l = line.split()
    arr1.append(int(l[0]))
    arr2.append(int(l[1]))
    dd1[int(l[1])] += 1
for item in arr1:
    ans+= item*dd1[item]

print(ans)