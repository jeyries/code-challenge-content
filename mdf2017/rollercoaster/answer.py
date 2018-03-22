
N = int(input())
poles = [int(input()) for _ in range(N)]
poles.sort()
soluce = []
for i in range(N//2):
    soluce.append(poles[i])
    soluce.append(poles[len(poles)-i-1])
if N % 2:
    soluce.append(poles[N//2])
#print(" ".join(map(str, soluce)))
for s in soluce:
    print(s)
