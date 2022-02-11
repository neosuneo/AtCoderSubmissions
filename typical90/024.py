n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 1 4
# 8 8
# 7+4 = 11

diff = 0
for i in range(n):
    diff += abs(A[i] - B[i])

if (k - diff) >= 0 and (k - diff) % 2 == 0:
    print('Yes')
else:
    print('No')
