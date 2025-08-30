import sys,heapq
input=sys.stdin.readline
n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
g=[[] for i in range(n+1)]
for i in range(m):
    g[u[i]].append((v[i],w[i]))
dist=[[10**18]*2 for i in range(n+1)]
pq=[]
dist[1][0]=0
dist[1][1]=0
heapq.heappush(pq,(0,1,0))
heapq.heappush(pq,(0,1,1))
while pq:
    d,x,p=heapq.heappop(pq)
    if d!=dist[x][p]:
        continue
    for y,c in g[x]:
        q=c%2
        if q!=p and d+c<dist[y][q]:
            dist[y][q]=d+c
            heapq.heappush(pq,(dist[y][q],y,q))
ans=min(dist[n])
if ans==10**18:
    print(-1)
else:
    print(ans)





# E. Parity Edges
# time limit per test1.5 seconds
# memory limit per test1024 megabytes
# You are given a directed weighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# Your task is to find the shortest distance from node 1
#  to node N
# , with an additional constraint: the path cannot contain two consecutive edges with the same parity (i.e., both even or both odd). If no such path exists, print −1
# .

# Input
# The first line contains two integers N,M(2≤N≤2×10^5,1≤M≤3×10^5)
#  — the number of vertices, total number of edges.

# The second line contains M
#  integers u1,u2,u3…um
#  (1≤ui≤N)
#  — where the i-th integer represents the node that is one endpoint of the i-th edge.

# The third line contains M
#  integers v1,v2,v3…vm
#  (1≤vi≤N)
#  — where the i-th integer represents the node that is the other endpoint of the i-th edge.

# The fourth line contains M
#  integers w1,w2,w3…wm
#  (1≤wi≤10^6)
#  — where the i-th integer represents the weight of the i-th edge.

# The i-th edge of this graph is from the i-th node in the second line to the i-th node in the third line.

# Output
# Print a single integer — the minimum distance from node 1
#  to node N
#  following the given constraint. If there is no valid path, print -1.

# Examples
# InputCopy
# 4 3
# 1 3 2
# 4 4 3
# 3 4 5
# OutputCopy
# 3
# InputCopy
# 6 5
# 1 4 1 6 4
# 2 1 6 2 6
# 3 3 4 3 4
# OutputCopy
# 4
# InputCopy
# 2 1
# 2
# 1
# 7
# OutputCopy
# -1
# InputCopy
# 5 7
# 1 1 4 5 2 3 2
# 4 5 3 4 4 5 3
# 3 8 2 6 6 4 3
# OutputCopy
# 8