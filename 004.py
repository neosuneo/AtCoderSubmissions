H, W = map(int, input().split())

rows = [0] * H
cols = [0] * W

mat = []

for i in range(H):
    row = list(map(int, input().split()))
    mat.append(row)
    rows[i] = sum(row)
    for j in range(W):
        cols[j] += row[j]


for i in range(H):
    row = []
    for j in range(W):
        row.append(rows[i] + cols[j] - mat[i][j])
    print(' '.join(map(str, row)))

