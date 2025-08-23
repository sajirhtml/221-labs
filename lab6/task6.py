from collections import deque

def solve():
    import sys
    inp = sys.stdin.readline
    n,m,s,q = map(int, inp().split())
    g = [[] for i in range(n+1)]
    for i in range(m):
        u,v = map(int, inp().split())
        g[u].append(v)
        g[v].append(u)
    src = list(map(int, inp().split()))
    dest = list(map(int, inp().split()))
    dist = [-1]*(n+1)
    queue = deque()
    for i in src:
        dist[i] = 0
        queue.append(i)
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if dist[v]==-1:
                dist[v] = dist[u]+1
                queue.append(v)
    res = []
    for i in dest:
        res.append(str(dist[i]))
    print(' '.join(res))
solve()




# F. Nearest Tour Destination
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an undirected unweighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops and no multiple edges.

# There are S
#  sources and Q
#  destinations. For each destination node, find the length of the shortest path from any source node to that destination. If a destination is unreachable from all sources, output −1
# .

# Input
# The first line contains four integers N,M,S,Q
#  1≤N≤2×10^5,0≤M≤3×10^5,1≤S≤N,1≤Q≤N
#  — the number of nodes, the number of edges, the number of source nodes, and the number of destination nodes.

# The next M
#  lines will contain two integers ui,vi(1≤ui,vi≤N)
#  — denoting there is an edge from node ui
#  to node vi
# .

# The next line contains S
#  (1≤Si≤N)
#  integers representing the source nodes, and the final line contains Q
#  (1≤Qi≤N)
#  integers representing the destination nodes. A node may appear both as a source and as a destination.

# Output
# The output should consist of Q
#  integers separated by spaces. The j
# -th integer denotes the length of the shortest path from any source node to the j
# -th destination node. If no such path exists for a destination node, print −1
#  for that destination. A node may be both a source and a destination, in which case the answer for that destination is 0
# .

# Examples
# InputCopy
# 8 6 2 4
# 1 2
# 2 3
# 4 5
# 6 7
# 7 8
# 2 6
# 1 6
# 3 5 6 8
# OutputCopy
# 2 -1 0 2 
# InputCopy
# 18 17 4 10
# 1 2
# 2 3
# 3 4
# 4 1
# 3 5
# 5 6
# 6 7
# 8 9
# 9 10
# 10 8
# 10 11
# 11 12
# 9 13
# 13 14
# 15 16
# 16 17
# 17 15
# 15 1 6 8
# 14 3 10 7 1 12 11 5 18 16
# OutputCopy
# 3 2 1 1 0 3 2 1 -1 1 