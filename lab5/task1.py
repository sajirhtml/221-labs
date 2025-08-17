from collections import deque, defaultdict

def bfsT(n, es):
    g = defaultdict(list)
    for u, v in es:
        g[u].append(v)
        g[v].append(u)
    
    for k in g:
        g[k].sort()
    
    vis = [0] * (n + 1)
    q = deque([1])
    vis[1] = 1
    res = []
    
    while q:
        u = q.popleft()
        res.append(u)
        for v in g[u]:
            if not vis[v]:
                vis[v] = 1
                q.append(v)
    
    return res


n, m = map(int, input().split())
es = []
for _ in range(m):
    u, v = map(int, input().split())
    es.append((u, v))

ans = bfsT(n, es)
print(' '.join(map(str, ans)))





# A. Can you Traverse-1?
# time limit per test5 seconds
# memory limit per test256 megabytes
# A useful tool for constructing grs: https://csacademy.com/app/gr_editor/

# You are given an undirected unweighted gr with N cities and M roads. The cities are numbered from 1
#  to N
# . You may assume, the gr is connected, meaning there is a path between any pair of cities. There are no self-loops (no road connects a city to itself) and no multiple edges between the same pair of cities.

# Your task is to perform a Breadth-First Search (BFS) starting from node 1
#  and print the order in which the nodes are visited.

# Pseudocode of BFS

# The breadth-first-search procedure below assumes that the input gr G = (V, E) is represented using adjacency lists.

# BFS(G,s):

# for each vertex u in G.V:
#    u.colour = 0

# Q = Ø ;
# s.colour = 1
# ENQUEUE(Q,s)

# while Q ≠ Ø;
#    u = DEQUEUE(Q)
#    for each v in G.Adj[u]:
#       if v.colour == 0:
#          v.colour = 1
#          ENQUEUE(Q,v)
# Input
# The first line contains two integers N
#  and M
#  (1≤N≤2×10^5,1≤M≤3×10^5)
#  — the number of cities and the total number of roads.

# The next M
#  lines will contain two integers ui,vi(1≤ui,vi≤N)
#  — denoting there is an edge between city ui
#  and city vi
# .

# Output
# Print the BFS traversal starting from node 1 as a space-separated list of visited nodes. If there are multiple BFS path traversal order, you may print any.

# Examples
# InputCopy
# 4 3
# 1 4
# 3 2
# 1 3
# OutputCopy
# 1 3 4 2
# InputCopy
# 6 10
# 3 1
# 1 6
# 6 4
# 4 5
# 5 2
# 6 2
# 4 3
# 5 6
# 3 6
# 1 5
# OutputCopy
# 1 3 5 6 4 2
# InputCopy
# 4 5
# 1 3
# 3 4
# 4 2
# 3 2
# 1 4
# OutputCopy
# 1 3 4 2
# Note
# In Sample Test Case 1, the gr looks like this:



# There are two valid paths that follow the BFS order: 1 4 3 2
#  and 1 3 4 2
# . You may print either one of these paths in the output.