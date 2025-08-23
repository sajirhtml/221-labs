from collections import deque
import sys
inp = sys.stdin.readline

def solve():
    n, m = map(int, inp().split())
    g = []
    for i in range(n + 1):
        g.append([])
    indeg = []
    for i in range(n + 1):
        indeg.append(0)

    for i in range(m):
        a, b = map(int, inp().split())
        g[a].append(b)
        indeg[b] += 1

    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    res = []
    while len(q) > 0:
        u = q.popleft()
        res.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(res) == n:
        print(*res)
    else:
        print(-1)

solve()





# A. Advising
# time limit per test1 second
# memory limit per test1024 megabytes
# In this problem, there are N courses in the curriculum and M requirements of the form "Course A has to be completed before course B".

# Your task is to find an order in which you can complete the courses. If there are multiple valid order, you may print any of them. If no such sequence exists, then print −1
# .

# Input
# The first line contains two integers N,M
#  (1≤N≤2×10^5,1≤M≤3×10^5)
#  — the number of courses and total requirements.

# The next M
#  lines will contain two integers Ai,Bi(1≤Ai,Bi≤N)
#  — Course A has to be completed before course B.

# Output
# Print an order in which you can complete the courses. Please note, that there could be multiple correct sequences. You can print any valid order that includes all the courses.

# If there is no valid sequence, print −1
# .

# Examples
# InputCopy
# 5 4
# 2 4
# 2 5
# 4 3
# 1 5
# OutputCopy
# 2 4 3 1 5
# InputCopy
# 8 8
# 6 4
# 6 2
# 4 2
# 2 1
# 1 7
# 7 5
# 5 8
# 8 3
# OutputCopy
# 6 4 2 1 7 5 8 3
# InputCopy
# 2 1
# 1 2
# OutputCopy
# 1 2
# InputCopy
# 4 6
# 1 2
# 1 3
# 4 1
# 2 3
# 2 4
# 4 3
# OutputCopy
# -1