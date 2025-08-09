N, M = map(int, input().split())
am = []
for ii in range(N):
    r = []
    for jj in range(N):
        r.append(0)
    am.append(r)

for kk in range(M):
    u, v, w = map(int, input().split())
    am[u-1][v-1] = w
for r in am:
    print(" ".join(map(str, r)))