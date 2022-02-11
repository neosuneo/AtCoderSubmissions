n = int(input())
A = list(map(int, input().split()))
q = int(input())
A = sorted(A)
B = []

def min_diff(rating):
    # bs 
    if rating <= A[0]:
        return A[0] - rating
    if rating >= A[n-1]:
        return rating - A[n-1]
    
    left = 0
    right = n - 1
    
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < rating:
            left = mid
        elif A[mid] > rating:
            right = mid
        else:
            return 0
    
    return min(rating - A[left], A[right] - rating)

for _ in range(q):
    B.append(int(input()))

for b in B:
    print(min_diff(b))


