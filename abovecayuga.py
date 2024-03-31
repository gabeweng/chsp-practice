from itertools import permutations
import math

whatever=0.00001 #can be changed, is our error margin

n = int(input())

points=[[0,0] for i in range(n)]

for i in range(n):
    points[i]=list(map(int, input().split()))

perms = list(permutations(points))

maxtriangles = 0
for perm in perms:
    # print(perm)
    numtriangles = 0
    for i in range(0,n-2,3):
        a = perm[i]
        b = perm[i+1]
        c = perm[i+2]
        dist1 = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        dist2 = math.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)
        dist3 = math.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)
        if dist1 + dist2 > dist3+whatever and dist1 + dist3 > dist2+whatever and dist2 + dist3 > dist1+whatever:
            numtriangles += 1
    # print(numtriangles)
    if numtriangles > maxtriangles:
        maxtriangles = numtriangles

print(maxtriangles)
