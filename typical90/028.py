import collections
import sys
sys.setrecursionlimit = 10**18
n = int(input())

D = collections.defaultdict(int)
L = []
for _ in range(n):
    L.append(list(map(int, input().split())))

size = 1001

M = [[0]*size for _ in range(size)]

# 1000**2 * 10000
for l in L:
    x1, y1, x2, y2 = l
    M[x1][y1] += 1
    M[x1][y2] -= 1
    M[x2][y1] -= 1
    M[x2][y2] += 1

for x in range(0, size):
    for y in range(1, size):
        M[x][y] += M[x][y-1] 

for y in range(0, size):
    for x in range(1, size):
        M[x][y] += M[x-1][y] 

#print(M)

C = [0]*(n+1)

for x in range(0, size):
    for y in range(0, size):
        C[M[x][y]] += 1

for i in range(1, n+1):
    print(C[i])

