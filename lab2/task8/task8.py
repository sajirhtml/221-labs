t = int(input())

for i in range(t):
    m, n = map(int, input().split())
    r = m + (m - 1) // (n - 1)
    print(r)