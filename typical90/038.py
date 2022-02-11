def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

a, b = map(int, input().split())

lcm = a * b // gcd(a, b)

if lcm > 10**18:
    print('Large')
else:
    print(lcm)

