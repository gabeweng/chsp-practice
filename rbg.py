#BACKGROUND: The problem uses 1 to n, while python uses 0 to n-1. We will need to convert.

w,l,h = list(map(int, input().split()))

arr=[[[[0,0,0] for i in range(h)] for j in range(l)] for k in range(w)] # 4D array with arr[w][l][h] being the RGB value of the pixel at (w,l,h)


for i in range(w):
    for j in range(l):
        for k in range(h):
            arr[i][j][k] = list(map(int, input().split())) #RGB value of pixel at (i,j,k)

numPixels = int(input())

for i in range(numPixels):
    sum = [0,0,0]
    n = 0
    x1,y1,z1,x2,y2,z2 = list(map(int, input().split()))
    x1-=1
    y1-=1
    z1-=1
    x2-=1
    y2-=1
    z2-=1
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                sum[0] += arr[x][y][z][0]
                sum[1] += arr[x][y][z][1]
                sum[2] += arr[x][y][z][2]
                n+=1
    print(sum[0]//n, sum[1]//n, sum[2]//n)