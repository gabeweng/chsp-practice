from itertools import permutations
n = int(input())

starts=list(map(int, input().split()))
ends=list(map(int, input().split()))

# print(starts, ends)

minttime= 0
for i in range(n):
    minttime += abs(starts[i]-ends[i])

perms = list(permutations(starts))

# print(perms)

for perm in perms:
    # print(perm,ends)
    
    maxtime = 0
    for i in range(n):
        if abs(perm[i]-ends[i]) > maxtime:
            maxtime = abs(perm[i]-ends[i])
    if maxtime < minttime:
        minttime = maxtime

print(minttime)
