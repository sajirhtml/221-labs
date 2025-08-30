import heapq,sys
n,m,s,d=map(int,sys.stdin.readline().split())
g=[[] for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,sys.stdin.readline().split())
    g[u].append((v,w))
    g[v].append((u,w))
inf=10**18
dist=[[inf,inf] for i in range(n+1)]
dist[s][0]=0
h=[(0,s)]
while h:
    du,u=heapq.heappop(h)
    for v,w in g[u]:
        nd=du+w
        if nd<dist[v][0]:
            dist[v][1]=dist[v][0]
            dist[v][0]=nd
            heapq.heappush(h,(nd,v))
        elif dist[v][0]<nd<dist[v][1]:
            dist[v][1]=nd
            heapq.heappush(h,(nd,v))
ans=dist[d][1]
if ans==inf:print(-1)
else:print(ans)





# F. Shortest Path Revisited
# time limit per test3 seconds
# memory limit per test1024 megabytes
# You are given a bidirectional weighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# There is a source and a destination. Your task is to find the cost of the second shortest path from the source node to the destination node. If no such path exists, print −1
# .

# Note: Second shortest path will be strictly greater than the shortest path

# Input
# The first line contains four integers N,M,S,D(2≤N≤2×10^5,1≤M≤3×10^5,1≤S,D≤N)
#  — the number of vertices, total number of edges, source, and destination.

# The next M
#  lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤106)
#  — there is an edge between the node ui
#  and the node vi
#  with a weight wi
# .

# Output
# If a valid path exists from S
#  to D
# , print the cost of the second shortest path from S
#  to D
# .
# If no such path exists, print −1
# .
# Examples
# InputCopy
# 4 3 2 3
# 2 1 3
# 2 3 5
# 3 4 3
# OutputCopy
# 11
# InputCopy
# 6 5 3 4
# 1 2 3
# 1 4 5
# 1 6 2
# 2 6 3
# 4 6 1
# OutputCopy
# -1
# InputCopy
# 2 1 2 2
# 2 1 5
# OutputCopy
# 10
# InputCopy
# 5 7 2 5
# 1 5 3
# 1 4 2
# 5 3 1
# 5 4 6
# 5 2 5
# 3 4 4
# 3 2 8
# OutputCopy
# 7