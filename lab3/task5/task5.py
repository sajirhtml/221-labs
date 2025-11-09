def pwr(x, y, z):
    res = 1
    x %= z
    while y:
        if y & 1:
            res = (res * x) % z
        x = (x * x) % z
        y >>= 1
    return res
 
def geo(s, t, m):
    if t == 1:
        return s % m
    if t & 1 == 0:
        half = geo(s, t >> 1, m)
        p = pwr(s, t >> 1, m)
        return (half * (1 + p)) % m
    else:
        return (geo(s, t - 1, m) + pwr(s, t, m)) % m
 
o = []
T = int(input())
for _ in range(T):
    A, N, M = map(int, input().split())
    o.append(geo(A, N, M))
print(*o, sep='\n')