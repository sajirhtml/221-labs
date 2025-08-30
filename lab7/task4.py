import sys,heapq
n,m,s,d=map(int,sys.stdin.readline().split())
w=list(map(int,sys.stdin.readline().split()))
g=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    g[u].append(v)
inf=10**18
dist=[inf]*(n+1)
dist[s]=w[s-1]
pq=[(w[s-1],s)]
while pq:
    c,u=heapq.heappop(pq)
    if c>dist[u]:
        continue
    for v in g[u]:
        nc=c+w[v-1]
        if nc<dist[v]:
            dist[v]=nc
            heapq.heappush(pq,(nc,v))
print(-1 if dist[d]==inf else dist[d])





# D. Beautiful Path
# time limit per test2 seconds
# memory limit per test1024 megabytes
# You are given an directed graph with N
#  nodes and M
#  edges. The graph contains no self-loops or multiple edges. The edges have no weight. The nodes are numbered from 1
#  to N
#  and have a weight. You need to find the cost of a path, if there is any, from node S
#  to node D
#  with the minimum cost. The cost of a path is the sum of the weights of the nodes in that path.

# Input
# The first line contains four integers N,M,S,D(2≤N≤2×10^5,1≤M≤3×10^5,1≤S,D≤N)
#  — the number of vertices, total number of edges, source, and destination.

# In the next line, there will be N integers w1,w2,w3…wn
#  (1≤wi≤10^6)
#  separated by spaces – representing the weights of each node.

# The next M
#  lines will contain two integers ui,vi(1≤ui,vi≤N)
#  — there is an edge from the node ui
#  to the node vi
# .

# Output
# If a valid path exists from S
#  to D
# , print the minimum cost of the path. Otherwise, print −1
# .

# Examples
# InputCopy
# 4 3 1 2
# 3 4 5 4
# 1 2
# 3 2
# 4 3
# OutputCopy
# 7
# InputCopy
# 6 5 5 3
# 3 3 4 3 4 1
# 1 2
# 4 1
# 1 6
# 6 2
# 4 6
# OutputCopy
# -1
# InputCopy
# 2 1 1 1
# 7 6
# 2 1
# OutputCopy
# 7
# InputCopy
# 5 7 3 5
# 3 8 2 6 6
# 1 5
# 1 4
# 5 3
# 4 5
# 2 5
# 3 4
# 2 3
# OutputCopy
# 14