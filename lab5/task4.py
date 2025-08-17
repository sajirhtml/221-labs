from collections import deque

def bfs(s, n, adj):
    d = [-1] * (n + 1)
    p = [-1] * (n + 1)
    q = deque([s])
    d[s] = 0
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                p[v] = u
                q.append(v)
    
    return d, p

def path(p, s, e):
    if p[e] == -1 and s != e:
        return None
    
    r = []
    c = e
    while c != -1:
        r.append(c)
        if c == s:
            break
        c = p[c]
    
    if r[-1] != s:
        return None
    
    return r[::-1]

n, m, s, d, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

ds, ps = bfs(s, n, adj)
dk, pk = bfs(k, n, adj)

if ds[k] == -1 or dk[d] == -1:
    print(-1)
else:
    p1 = path(ps, s, k)
    p2 = path(pk, k, d)
    
    if p1 is None or p2 is None:
        print(-1)
    else:
        fp = p1 + p2[1:]
        print(len(fp) - 1)
        print(" ".join(map(str, fp)))




#         D. Through the Jungle
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a directed unweighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# You have to find a shortest path from node S
#  to node D
#  that passes through node K
# . If multiple such paths exist, print any one of them. If no such path exists, print −1
# .

# Input
# The first line contains five integers N,M,S,D,K
#  (1≤N≤2×10^5,1≤M≤3×10^5,1≤S,
# D,K≤N)
#  — the number of vertices, total number of edges, source, destination and the mandatory node that must be included in the path.

# The next M
#  lines will contain two integers ui,vi(1≤ui,vi≤N)
#  — denoting there is an edge from city ui
#  to city vi
# .

# Output
# If a valid path exists from S
#  to D
#  through K
# , print the length of the path (number of edges) on the first line.
# On the second line, print the nodes in the path in order from S
#  to D
# .
# If no such path exists, print −1
# .
# Examples
# InputCopy
# 5 10 5 3 5
# 2 5
# 5 1
# 4 5
# 3 5
# 1 2
# 2 4
# 3 2
# 1 4
# 1 3
# 3 4
# OutputCopy
# 2
# 5 1 3
# InputCopy
# 5 4 2 5 3
# 5 1
# 3 1
# 2 3
# 2 4
# OutputCopy
# -1
# InputCopy
# 8 7 3 2 4
# 7 2
# 6 7
# 7 3
# 2 4
# 1 2
# 8 4
# 5 1
# OutputCopy
# -1
# InputCopy
# 6 6 2 2 2
# 5 1
# 1 2
# 1 4
# 5 2
# 4 5
# 3 2
# OutputCopy
# 0
# 2