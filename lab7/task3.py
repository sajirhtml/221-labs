import sys,heapq
n,m=map(int,sys.stdin.readline().split())
g=[[] for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,sys.stdin.readline().split())
    g[u].append((v,w))
    g[v].append((u,w))
d=[10**9]*(n+1)
d[1]=0
h=[(0,1)]
while h:
    x,u=heapq.heappop(h)
    if x>d[u]:
        continue
    for v,w in g[u]:
        y=max(d[u],w)
        if y<d[v]:
            d[v]=y
            heapq.heappush(h,(y,v))
for i in range(1,n+1):
    if d[i]==10**9:
        d[i]=-1
print(*d[1:])





# C. Minimize the Danger
# time limit per test2 seconds
# memory limit per test1024 megabytes
# You are in a city with N
#  cities connected by M
#  bi-directional roads. Each road has a danger level, where a higher number means the road is more dangerous.

# You start in city 1
#  and need to go to every other city. The goal is to find the minimum danger level you would face to reach each city from city 1
# . The danger of a path is defined as the highest danger level of any road on that path.

# For each city, find the minimum danger level of the path from city 1
# . If a city is not reachable from city 1
# , print −1
# . The danger of reaching city 1
#  is always 0
# .

# Input
# The first line contains two integers N,M(2≤N≤2⋅10^5,1≤M≤3⋅10^5)
#  — the number of cities, the total number of roads.

# The next M
#  lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤10^6)
#  — node ui
#  is connected to node vi
#  with a weight wi
# .

# Output
# Output n
#  integers, where i
# -th integer represents the minimum danger level you'd have to face in order to go from city 1
#  to city i
# .

# Examples
# InputCopy
# 4 3
# 2 1 3
# 2 3 5
# 3 4 3
# OutputCopy
# 0 3 5 5
# InputCopy
# 6 5
# 1 2 3
# 1 4 5
# 1 6 2
# 2 6 3
# 4 6 1
# OutputCopy
# 0 3 -1 2 -1 2
# InputCopy
# 2 1
# 2 1 5
# OutputCopy
# 0 5
# InputCopy
# 5 7
# 1 5 3
# 1 4 2
# 5 3 1
# 5 4 6
# 5 2 5
# 3 4 4
# 3 2 8
# OutputCopy
# 0 5 3 2 3