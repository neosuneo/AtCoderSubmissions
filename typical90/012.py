import sys
sys.setrecursionlimit(10**7)
h, w = map(int, input().split())
q = int(input())

Q = []
for _ in range(q):
    Q.append(list(map(int, input().split())))

P = [-1] * (2010*2010)

r_step = 2010

def find_parent(idx):
    if P[idx] == idx:
        return idx
    else:
        P[idx] = find_parent(P[idx])
        return P[idx]

def color(idx):
    P[idx] = idx
    for neibor in [idx-r_step, idx+r_step, idx+1, idx-1]:
        if 0 <= neibor <= r_step**2-1:
            if P[neibor] != -1:
                parent = find_parent(neibor)
                P[parent] = idx

for q in Q:
    if q[0] == 1:
        color(q[1] * r_step + q[2])
    else:
        c1 = q[1] * r_step + q[2]
        c2 = q[3] * r_step + q[4]
        if P[c1] != -1 and P[c2] != -1 and find_parent(c1) == find_parent(c2):
            print("Yes")
        else:
            print("No")
