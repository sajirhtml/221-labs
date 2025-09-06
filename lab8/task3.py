import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
NEG=-10**18
n,m=map(int,input().split())
es=[]
for _ in range(m):
    a,b,w=map(int,input().split()); es.append((w,a-1,b-1))
es_sorted=sorted(enumerate(es),key=lambda x:x[1][0])
p=list(range(n))
r=[0]*n
def f(x):
    while p[x]!=x:
        p[x]=p[p[x]]
        x=p[x]
    return x
def unite(a,b):
    a=f(a); b=f(b)
    if a==b: return False
    if r[a]<r[b]: a,b=b,a
    p[b]=a
    if r[a]==r[b]: r[a]+=1
    return True
used=[False]*m
mst=0
g=[[] for _ in range(n)]
for idx,(w,u,v) in es_sorted:
    if unite(u,v):
        used[idx]=True
        mst+=w
        g[u].append((v,w))
        g[v].append((u,w))
if sum(1 for i in range(n) if f(i)==f(0))!=n:
    print(-1); exit()

LOG=(n-1).bit_length()+1
up=[[ -1]*n for i in range(LOG)]
m1=[[NEG]*n for j in range(LOG)]
m2=[[NEG]*n for k in range(LOG)]
depth=[0]*n

def dfs(u,par):
    for v,w in g[u]:
        if v==par: continue
        depth[v]=depth[u]+1
        up[0][v]=u
        m1[0][v]=w
        m2[0][v]=NEG
        dfs(v,u)
dfs(0,-1)
for k in range(1,LOG):
    for v in range(n):
        a=up[k-1][v]
        if a==-1:
            up[k][v]=-1
            m1[k][v]=m1[k-1][v]
            m2[k][v]=m2[k-1][v]
        else:
            up[k][v]=up[k-1][a]
            vals=[m1[k-1][v],m2[k-1][v],m1[k-1][a],m2[k-1][a]]
            mx1=max(vals)
            vals.remove(mx1)
            mx2=max(vals)
            m1[k][v]=mx1
            m2[k][v]=mx2

def query(u,v):
    x1=NEG; x2=NEG
    if depth[u]<depth[v]: u,v=v,u
    dif=depth[u]-depth[v]
    k=0
    while dif:
        if dif&1:
            vals=[x1,x2,m1[k][u],m2[k][u]]
            mx1=max(vals); vals.remove(mx1); mx2=max(vals)
            x1,x2=mx1,mx2
            u=up[k][u]
        dif>>=1; k+=1
    if u==v: return x1,x2
    for k in range(LOG-1,-1,-1):
        if up[k][u]!=-1 and up[k][u]!=up[k][v]:
            vals=[x1,x2,m1[k][u],m2[k][u],m1[k][v],m2[k][v]]
            mx1=max(vals); vals.remove(mx1); mx2=max(vals)
            x1,x2=mx1,mx2
            u=up[k][u]; v=up[k][v]
    vals=[x1,x2,m1[0][u],m2[0][u],m1[0][v],m2[0][v]]
    mx1=max(vals); vals.remove(mx1); mx2=max(vals)
    return mx1,mx2

ans=10**30
for i,(w,u,v) in enumerate(es):
    if used[i]: continue
    a,b=query(u,v)
    if w>a and a>NEG:
        cand=mst+w-a
        if cand>mst: ans=min(ans,cand)
    elif a>NEG and b>NEG and w>b:
        cand=mst+w-b
        if cand>mst: ans=min(ans,cand)
print(ans if ans<10**29 else -1)






# C. Again MST
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a bidirectional weighted graph with N
#  nodes and M
#  edges. The nodes are numbered from 1
#  to N
# . The graph contains no self-loops or multiple edges.

# Your task is to find the total cost of the second-best Minimum Spanning Tree. If no such tree exists, print −1
# .

# Note: The second-best MST must have a total weight strictly greater than that of the best (minimum) MST.

# Input
# The first line contains four integers N,M(2≤N≤10^3,1≤M≤2×10^3)
#  — the number of vertices, total number of edges.

# The next M
#  lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤10^6)
#  — there is an edge between the node ui
#  and the node vi
#  with a weight wi
# .

# Output
# Output the total cost of the second-best Minimum Spanning Tree. If no such tree exists, print −1
# .

# Examples
# InputCopy
# 6 7
# 1 2 1
# 2 3 2
# 3 1 3
# 1 4 5
# 4 5 4
# 5 6 5
# 6 4 5
# OutputCopy
# 18
# InputCopy
# 5 5
# 1 2 3
# 2 3 4
# 3 4 5
# 4 5 1
# 5 1 2
# OutputCopy
# 11