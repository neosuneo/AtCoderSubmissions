n = int(input())

username_set = set()
for i in range(1, n+1):
    s = input()
    if s not in username_set:
        print(i)
        username_set.add(s)

