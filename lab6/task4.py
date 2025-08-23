import sys
from collections import deque

def bfs(s, g, n):
    d = [-1] * (n + 1)
    q = deque()
    q.append(s)
    d[s] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    m = 0
    node = s
    for i in range(1, n + 1):
        if d[i] > m:
            m = d[i]
            node = i
    return node, m, d

def solve():
    inp = sys.stdin.readline
    n = int(inp())
    g = [[] for i in range(n + 1)]
    for i in range(n - 1):
        u, v = map(int, inp().split())
        g[u].append(v)
        g[v].append(u)
    a, x, y = bfs(1, g, n)
    b, dist, d = bfs(a, g, n)
    print(dist)
    print(a, b)
solve()



# D. What's the Diameter?
# time limit per test1 second
# memory limit per test1024 megabytes
# You are given an undirected connected graph with N
#  nodes and N−1
#  edges. Your task is to find two nodes such that the path between those two nodes is the longest possible in the graph.

# Input
# The first line contains one integer N
#  (2≤N≤200000)
#  — the number of nodes.

# The next N−1
#  lines will contain two integers ui
# , vi
#  (1≤ui,vi≤N)
#  — denoting there is a bidirectional road between ui
#  and vi
# .

# Output
# On the first line, print a single integer — the length of the longest path.

# On the second line, print two integers A and B — the nodes that form this longest path. If multiple pairs exist, you may print any one.

# Examples
# InputCopy
# 5
# 5 1
# 1 4
# 4 2
# 3 2
# OutputCopy
# 4
# 3 5
# InputCopy
# 5
# 1 2
# 5 3
# 3 2
# 2 4
# OutputCopy
# 3
# 5 1
# InputCopy
# 8
# 1 7
# 7 3
# 3 6
# 6 5
# 5 2
# 2 8
# 8 4
# OutputCopy
# 7
# 4 1
# InputCopy
# 7
# 7 5
# 5 6
# 6 1
# 1 3
# 3 4
# 4 2
# OutputCopy
# 6
# 7 2