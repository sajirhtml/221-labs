import sys,heapq
from collections import deque
input=sys.stdin.readline
n,m,s,d=map(int,input().split())
if m:
    u=list(map(int,input().split()))
    v=list(map(int,input().split()))
    g=[[] for i in range(n+1)]
    for i in range(m):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])
    for i in range(1,n+1):
        g[i].sort()
    dist=[-1]*(n+1)
    par=[-1]*(n+1)
    q=deque([s])
    dist[s]=0
    while q:
        x=q.popleft()
        if x==d:break
        for y in g[x]:
            if dist[y]==-1:
                dist[y]=dist[x]+1
                par[y]=x
                q.append(y)
    if dist[d]==-1:
        print(-1)
    else:
        print(dist[d])
        path=[]
        cur=d
        while cur!=-1:
            path.append(cur)
            cur=par[cur]
        print(*path[::-1])
else:
    if s==d:
        print(0)
        print(s)
    else:
        print(-1)




# C. Lightning McQueen
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an undirected unweighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# There is a source and a destination. Your task is to find the shortest distance from the source node to destination node and print the path taken. If multiple shortest paths exist, print the one that is lexicographically smallest.

# A path P1=[a1,a2,…an]
#  is lexicographically smaller than a path P2=[b1,b2,…bm]
#  if at the first position where they differ, ai<bi
# . For example, [1,4,3]
#  is smaller than [1,5,7,1]
# .

# If no path exists, print −1
# .

# Input
# The first line contains four integers N,M,S,D
#  (1≤N≤2×10^5,0≤M≤3×10^5,1≤S,
# D≤N)
#  — the number of vertices, total number of edges, source and destination.

# The second line contains M
#  integers u1,u2,u3…um
#  (1≤ui≤N)
#  — where the i-th integer represents the node that is one endpoint of the i-th edge.

# The third line contains M
#  integers v1,v2,v3…vm
#  (1≤vi≤N)
#  — where the i-th integer represents the node that is other endpoint of the i-th edge.

# The i-th edge of this graph is between the i-th node in the second line and the i-th node in the third line.

# Output
# If a path exists, print the length of the shortest path (number of edges) on the first line.
# On the second line, print the lexicographically smallest shortest path from source to destination.
# If no path exists, print -1.
# Examples
# InputCopy
# 5 10 5 3
# 2 1 5 3 1 4 2 4 1 4
# 5 5 4 5 2 2 3 1 3 3
# OutputCopy
# 1
# 5 3
# InputCopy
# 5 4 2 5
# 5 1 2 4
# 1 3 3 2
# OutputCopy
# 3
# 2 3 1 5
# InputCopy
# 8 7 3 2
# 7 7 3 2 2 8 5
# 2 6 7 4 1 4 1
# OutputCopy
# 2
# 3 7 2
# InputCopy
# 6 6 6 5
# 1 2 1 5 5 3
# 5 1 4 2 4 2
# OutputCopy
# -1
# InputCopy
# 1 0 1 1


# OutputCopy
# 0
# 1