from collections import deque
import sys
input = sys.stdin.readline

R, H = map(int, input().split())
g = [list(input().strip()) for a in range(R)]

v = [[False]*H for a in range(R)]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    v[sr][sc] = True
    d = 0
    if g[sr][sc] == 'D':
        d += 1
    
    while q:
        r, c = q.popleft()
        for ra, ca in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+ra, c+ca
            if 0 <= nr < R and 0 <= nc < H:
                if not v[nr][nc] and g[nr][nc] != '#':
                    v[nr][nc] = True
                    if g[nr][nc] == 'D':
                        d += 1
                    q.append((nr, nc))
    return d

m = 0
for i in range(R):
    for j in range(H):
        if not v[i][j] and g[i][j] != '#':
            m = max(m, bfs(i, j))

print(m)





# You are given a 2D grid with R
#  rows and H
#  columns.

# Each cell in the grid is one of the following:

# .
#  — Empty cell: You can move into this cell.
# D
#  — Cell with a diamond: You can move into this cell and collect the diamond.
# #
#  — Obstacle: You cannot move into this cell.
# You may start from any non-obstacle cell and move in the four directions: up, down, left, or right. Your goal is to choose a starting cell such that you can collect the maximum number of diamonds

# Input
# The first line contains two integers R
#  and H
#  (1≤R,H≤1000)
#  — the number of rows and columns of the grid. The next R
#  lines each contain H
#  characters, describing the grid.

# Output
# Print a single integer — the maximum number of diamonds you can collect starting from a valid cell.

# Examples
# InputCopy
# 5 5
# .#.DD
# ##.#.
# ####D
# #DDD#
# #..DD
# OutputCopy
# 5
# InputCopy
# 5 5
# D####
# ##.D#
# #..D#
# ###D#
# ..##D
# OutputCopy
# 3
# InputCopy
# 5 5
# .....
# ####.
# #..#.
# ####.
# .....
# OutputCopy
# 0
# InputCopy
# 1 5
# D....
# OutputCopy
# 1
# InputCopy
# 9 11
# .#..D...D..
# .#.#######.
# D#.#..D..#.
# D#D#.###.#D
# .#.#..D#.#.
# .#.#####.#D
# D#..D...D#.
# .#########.
# ...D..D...D
# OutputCopy
# 15