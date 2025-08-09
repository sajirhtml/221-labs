a = 0
b = 0
arr = []
N = int(input())
n = input()
n = list(map(int,n.split()))
M = int(input())
m = input()
m = list(map(int,m.split()))

while True:
        if a >= N or b >= M: break
        elif m[b] < n[a]:
            arr.append(m[b])
            b += 1
        elif n[a] < m[b]:
            arr.append(n[a])
            a += 1
        else:
            arr.append(n[a])
            a += 1

while a < N:
    arr.append(n[a])
    a += 1

while b < M:
    arr.append(m[b])
    b += 1

print(*arr)