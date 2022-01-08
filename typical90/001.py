"""
001 - Yokan Party（★4）
https://atcoder.jp/contests/typical90/tasks/typical90_a
"""

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)
ok_score = 1
ng_score = L // (K + 1) + 1

def validate_score(score):
    start = 0
    count = 0
    for i in range(N+1):
        if A[i] - start >= score:
            count += 1
            start = A[i]
            if count >= K+1:
                return True
    return False

# binary search
while ng_score - ok_score != 1:
    mid_score = (ok_score + ng_score) // 2
    if validate_score(mid_score):
        ok_score = mid_score
    else:
        ng_score = mid_score
    
print(ok_score)