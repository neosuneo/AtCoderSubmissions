h, w = map(int, input().split())

# 2 3
# *** 
# ***
if h == 1:
    print(w)
elif w == 1:
    print(h)
else:
    print(((h + 1) // 2) * ((w + 1) // 2))
