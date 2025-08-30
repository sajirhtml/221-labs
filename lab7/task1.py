import sys,heapq

def solve():
    inp=sys.stdin.readline
    n,m,s,d=map(int,inp().split())
    u=list(map(int,inp().split()))
    v=list(map(int,inp().split()))
    w=list(map(int,inp().split()))
    g=[]
    k=0
    while k<n+1:
        g.append([])
        k+=1
    i=0
    while i<m:
        g[u[i]].append((v[i],w[i]))
        i+=1
    dist=[10**18]*(n+1)
    par=[-1]*(n+1)
    dist[s]=0
    pq=[(0,s)]
    while pq:
        x,y=heapq.heappop(pq)
        if x>dist[y]:
            continue
        j=0
        while j<len(g[y]):
            nx,wt=g[y][j]
            if dist[nx]>x+wt:
                dist[nx]=x+wt
                par[nx]=y
                heapq.heappush(pq,(dist[nx],nx))
            j+=1
    if dist[d]==10**18:
        print(-1)
        return
    print(dist[d])
    path=[]
    cur=d
    while cur!=-1:
        path.append(cur)
        cur=par[cur]
    path.reverse()
    print(*path)

solve()





# A. Shortest Path
# time limit per test1 second
# memory limit per test1024 megabytes
# You are given an directed weighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# There is a source and a destination. Your task is to find the shortest distance from the source node to the destination node and print the path taken. If multiple shortest paths exist, print any one of them. If no such path exists, print −1
# .

# Input
# The first line contains four integers N,M,S,D(2≤N≤2×10^5,1≤M≤3×10^5,1≤S,D≤N)
#  — the number of vertices, total number of edges, source and destination.

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
#  (1≤wi≤106)
#  — where the i-th integer represents the weight of the i-th edge.

# The i-th edge of this graph is from the i-th node in the second line to the i-th node in the third line.

# Output
# If a valid path exists from S
#  to D
# , print the shortest distance S
#  to D
#  on the first line.
# On the second line, print the nodes in the path in order from S
#  to D
# . If multiple shortest paths exist, print any one of them.
# If no such path exists, print −1
# .
# Examples
# InputCopy
# 4 3 4 2
# 1 3 4
# 2 2 3
# 3 4 5
# OutputCopy
# 9
# 4 3 2
# InputCopy
# 6 5 1 5
# 1 4 1 6 4
# 2 1 6 2 6
# 3 3 4 3 4
# OutputCopy
# -1
# InputCopy
# 2 1 2 1
# 2
# 1
# 7
# OutputCopy
# 7
# 2 1
# InputCopy
# 5 7 2 4
# 1 1 5 4 2 3 2
# 5 4 3 5 5 4 3
# 3 8 2 6 6 4 3
# OutputCopy
# 7
# 2 3 4