import sys
from collections import deque

def main():
    inp = sys.stdin.readline
    n, m = map(int, inp().split())
    g = [[] for a in range(n+1)]
    indeg = [0]*(n+1)
    for a in range(m):
        u, v = map(int, inp().split())
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(1, n+1) if indeg[i]==0])
    c = 0
    while q:
        x = q.popleft()
        c += 1
        for y in g[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    print("NO" if c == n else "YES")

main()





# You are given a directed unweighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# Write a code to find if there is any cycle in the graph. In graph theory, a cycle in a graph is a non-empty trail in which only the first and last vertices are equal. [Wikipedia]

# Input
# The first line contains four integers N
#  and M
#  (1≤N≤2×10^5,1≤M≤2×10^5) 
#  — the number of vertices and total number of edges.

# The next M
#  lines will contain two integers ui,vi(1≤ui,vi≤N)
#  — denoting there is an edge from city ui
#  to city vi
# .

# Output
# Print YES if the graph contains any cycle, otherwise print NO.

# Examples
# InputCopy
# 4 7
# 1 3
# 1 2
# 2 4
# 3 1
# 2 3
# 4 3
# 4 1
# OutputCopy
# YES
# InputCopy
# 6 5
# 6 4
# 6 3
# 4 5
# 6 2
# 4 1
# OutputCopy
# NO