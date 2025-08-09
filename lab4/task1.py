N, M = map(int, input().split())
am = []
for ii in range(N):
    r = []
    for jj in range(N):
        r.append(0)
    am.append(r)

for kk in range(M):
    u, v, w = map(int, input().split())
    am[u-1][v-1] = w
for r in am:
    print(" ".join(map(str, r)))


#     A. Adjacency Matrix Representation
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Each edge represents a direct connection between two nodes. There is no self loop or multi edge.

# Input
# The first line contains two integers N and M (1≤N≤100,0≤M≤N(N−1)/2)
#  — the number of vertices and the total number of edges.

# The next M lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤1000)
#  — denoting there is an edge from node ui
#  to vi
#  with cost wi
# .

# Output
# The output consists of an N×N
#  adjacency matrix representing the directed weighted graph. Each row corresponds to a node, and each column represents its directed edges to other nodes. The value at position (i,j)
#  denotes the weight of the edge from node i
#  to node j
# . If there is no edge, the value is 0.

# Examples
# InputCopy
# 6 7
# 1 5 6
# 6 3 5
# 1 3 9
# 3 4 7
# 4 6 1
# 5 6 8
# 6 1 6
# OutputCopy
# 0 0 9 0 6 0 
# 0 0 0 0 0 0 
# 0 0 0 7 0 0 
# 0 0 0 0 0 1 
# 0 0 0 0 0 8 
# 6 0 5 0 0 0 
# InputCopy
# 4 3
# 1 3 8
# 3 2 5
# 1 4 2
# OutputCopy
# 0 0 8 2 
# 0 0 0 0 
# 0 5 0 0 
# 0 0 0 0 