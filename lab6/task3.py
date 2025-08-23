from collections import deque
import sys

def solve():
    r = sys.stdin.readline
    n = int(r())
    x1, y1, x2, y2 = map(int, r().split())
    v = [[0]*n for i in range(n)]
    d = [[-1]*n for i in range(n)]
    mv = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (1, -2), (-1, 2), (-1, -2)]
    q = deque()
    q.append((x1-1, y1-1))
    v[x1-1][y1-1] = 1
    d[x1-1][y1-1] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in mv:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
                v[nx][ny] = 1
                d[nx][ny] = d[x][y]+1
                q.append((nx, ny))
    print(d[x2-1][y2-1])

solve()





# C. The Knight of Königsberg
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an N×N
#  chessboard and the initial position (x1,y1)
#  of a Knight piece. You need to find the minimum number of moves the Knight needs to reach the target position (x2,y2)
# . If it is not possible to reach the target, print −1
# .

# Moves of a Knight in Chess
# The Knight can move one step in any of the 8 possible directions as shown in the picture.

# Input
# The first line contains an integer (1≤N≤2×10^3)
#  — the size of the chessboard.

# The second line contains four integers (1≤x1,y1,x2,y2≤N)
#  — the initial position (x1,y1)
#  and the target position (x2,y2)
#  of the Knight on the chessboard.

# Output
# Print the minimum number of moves the Knight needs to reach the target position. If it's not possible, print −1
# .

# Examples
# InputCopy
# 3
# 1 2 1 3
# OutputCopy
# 3
# InputCopy
# 3
# 1 1 2 2
# OutputCopy
# -1
# InputCopy
# 10
# 8 4 3 1
# OutputCopy
# 4