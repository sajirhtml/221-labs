import sys,heapq

def solve():
    n,m,s,t=map(int,input().split())
    g=[[] for i in range(n+1)]
    for i in range(m):
        u,v,w=map(int,input().split())
        g[u].append((v,w))
    def dijk(st):
        d=[10**18]*(n+1)
        d[st]=0
        h=[(0,st)]
        while h:
            x,u=heapq.heappop(h)
            if x>d[u]:
                continue
            for v,w in g[u]:
                if d[v]>x+w:
                    d[v]=x+w
                    heapq.heappush(h,(d[v],v))
        return d
    da=dijk(s)
    db=dijk(t)
    ans=10**18
    node=-1
    for i in range(1,n+1):
        if da[i]<10**18 and db[i]<10**18:
            cur=max(da[i],db[i])
            if cur<ans or (cur==ans and (node==-1 or i<node)):
                ans=cur
                node=i
    if node==-1:
        print(-1)
    else:
        print(ans,node)

solve()





# B. Where to Meet?
# time limit per test2 seconds
# memory limit per test1024 megabytes
# Alice and Bob are in a hurry to meet each other and have to traverse through a directed graph with weighted edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# Alice starts from node S
#  and Bob starts from node T
# . They want to find a common node in the graph where they can meet each other in the minimum amount of time. Alice or Bob can wait at any node if they want to.

# Input
# The first line contains four integers N,M,S,T(2≤N≤2×10^5,1≤M≤3×10^5,1≤S,T≤N)
#  — the number of vertices, the total number of edges, the starting node of Alice, and the starting node of Bob.

# The next M
#  lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤10^6)
#  — there is a edge from the node ui
#  to the node vi
#  with a weight wi
# .

# Output
# Print two integers separated by a space: the minimum time required for Alice and Bob to meet, and the node where they meet. If there are multiple such nodes, print the smallest node. If no such node exists, print −1
# .

# Examples
# InputCopy
# 5 5 1 5
# 1 2 1
# 2 3 1
# 5 3 2
# 1 4 2
# 5 4 2
# OutputCopy
# 2 3
# InputCopy
# 6 5 1 5
# 1 2 3
# 4 1 3
# 1 6 4
# 6 2 3
# 4 6 4
# OutputCopy
# -1
# InputCopy
# 2 1 2 2
# 2 1 7
# OutputCopy
# 0 2
# InputCopy
# 5 7 2 5
# 1 5 3
# 1 4 8
# 5 3 2
# 4 5 6
# 2 5 6
# 3 4 4
# 2 3 3
# OutputCopy
# 3 3