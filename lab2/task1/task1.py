import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = N - 1

while l < r:
    total = arr[l] + arr[r]
    if total == S:
        print(l + 1, r + 1)
        sys.exit()
    elif total < S:
        l += 1
    else:
        r -= 1

print(-1)