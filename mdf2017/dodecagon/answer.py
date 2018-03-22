
#*
#* SOLUTION by ISOGRAD
#*
n = int(input())

t = [['.' for j in range(n)] for i in range(n)]

m = n // 2

for i in range(n):
    for j in range(n):
        x = abs(i - m)
        y = abs(j - m)
        d = max(x,y)
        if x == y:
            d += 1
        if d % 2 == m % 2:
            t[i][j] = '*'
        else:
            t[i][j] = '#'

t[0][0] = '.'
t[0][n-1] = '.'
t[n-1][0] = '.'
t[n-1][n-1] = '.'
t[m][m] = t[m][m-1]

for l in t:
    print("".join(l))

