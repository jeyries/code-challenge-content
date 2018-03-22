
#**************************************
#* Solution by Isograd
#**************************************
h = int(input())
l = int(input())
t = [input() for i in range(h)]

ii = -1
jj = -1

for i in range(h):
    for j in range(l):
        if t[i][j] == 'x':
            ii = i
            jj = j

visited = [[False for j in range(l)] for i in range(h)]
count = 0

def dfs(i,j):
    global count
    nbhood = [(i+x, j+y) for x in [-1,0,1] for y in [-1,0,1]
              if 0 <= i+x and i+x < h and 0 <= j+y and j+y < l]
    count += 1
    visited[i][j] = True
    if all(t[x][y] != '*' for (x,y) in nbhood):
        for (x,y) in nbhood:
            if not visited[x][y]:
                dfs(x,y)

dfs(ii,jj)
print(count)

