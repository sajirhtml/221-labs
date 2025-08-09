import sys
import math
input = sys.stdin.readline

N, Q = map(int, input().split())
g = []
for i in range(N + 1):
    g.append([])

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if math.gcd(i, j) == 1:
            g[i].append(j)
            g[j].append(i)

for i in range(1, N+1):
    g[i].sort()

for i in range(Q):
    x, k = map(int, input().split())
    if k <= len(g[x]):
        print(g[x][k-1])
    else:
        print(-1)




# H. Coprime Graph
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an integer N
# . Construct an undirected graph with N
#  nodes, where each node i
#  is connected to all node j
#  such that gcd(i,j)=1
#  where 1≤i,j≤N
#  and i≠j
# .

# For example,for N=6
# , the graph will be, G=[[2,3,4,5,6],[1,3,5],[1,2,4,5],[1,3,5],
# [1,2,3,4,6],
# [1,5]]
# .

# Now, there will be Q
#  queries. Each query consists of two integers X
#  and K
# . For each query, you have to determine the K−th
#  smallest node connected to node X
# .

# Input
# The first line contains two integers N and Q (1≤N≤2×10^3,1≤Q≤3×10^5)
#  — the number of vertices and the total number of queries.

# The next Q lines contain two integers X and K (1≤X≤N,1≤K≤10^6)
# , representing a query.

# Output
# For each query, output the K−th
#  smallest node connected to node X
# . If there are fewer than K
#  neighbors of X
# , then print -1.

# Examples
# InputCopy
# 5 6
# 1 3
# 3 1
# 4 2
# 5 5
# 3 4
# 5 2
# OutputCopy
# 4
# 1
# 3
# -1
# 5
# 2
# InputCopy
# 2000 3
# 903 24
# 702 563
# 942 50
# OutputCopy
# 41
# 1829
# 149
# InputCopy
# 1 1
# 1 1
# OutputCopy
# -1
# InputCopy
# 2 1
# 2 1
# OutputCopy
# 1
# Note
# Explanation of the First Sample (Let's go through the queries):

# Query (1, 3): The neighbors of node 1 are [2, 3, 4, 5]. Sorted: [2, 3, 4, 5]. The 3rd smallest is 4. Output: 4.

# Query (3, 1): The neighbors of node 3 are [1, 2, 4, 5]. Sorted: [1, 2, 4, 5]. The 1st smallest is 1. Output: 1.

# Query (4, 2): The neighbors of node 4 are [1, 3, 5]. Sorted: [1, 3, 5]. The 2nd smallest is 3. Output: 3.

# Query (5, 5): The neighbors of node 5 are [1, 2, 3, 4]. There are only 4 neighbors, so the 5th smallest does not exist. Output: -1.

# Query (3, 4): The neighbors of node 3 are [1, 2, 4, 5]. Sorted: [1, 2, 4, 5]. The 4th smallest is 5. Output: 5.

# Query (5, 2): The neighbors of node 5 are [1, 2, 3, 4]. Sorted: [1, 2, 3, 4]. The 2nd smallest is 2. Output: 2.