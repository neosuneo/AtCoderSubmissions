n = int(input())


A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

ans = 0
for i in range(n):
    ans += abs(A[i]-B[i])

print(ans)
