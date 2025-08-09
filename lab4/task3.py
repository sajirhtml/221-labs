N = int(input())
am = []
for i in range(N):
    r = []
    for j in range(N):
        r.append(0)
    am.append(r)

for i in range(N):
    d = list(map(int, input().split()))
    k = d[0]
    n = d[1:]
    for idx in range(k):
        node = n[idx]
        am[i][node] = 1

for i in range(N):
    for j in range(N):
        print(am[i][j], end=' ')
    print()



# C. Graph Metamorphosis
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a directed unweighted graph with N nodes in an adjacency list format. The nodes are numbered from 0 to N-1. Your task is to convert it into an adjacency matrix representation.

# Input
# The first line contains a integer N (1≤N≤100
# ) — the number of vertices.

# The next N lines describe the adjacency list:

# The i
# -th line starts with an integer k
# , indicating the number of nodes adjacent to node i
# .
# The next k
#  space-separated integers represent the nodes adjacent to node i
# .
# Nodes are numbered from 0 to N-1.
# Output
# Print an N×N adjacency matrix, where the cell at row i and column j

# 1 if there is an edge between nodes i and j
# 0 otherwise.
# Examples
# InputCopy
# 5
# 2 1 2
# 1 0
# 1 0
# 1 4
# 1 3
# OutputCopy
# 0 1 1 0 0 
# 1 0 0 0 0 
# 1 0 0 0 0 
# 0 0 0 0 1 
# 0 0 0 1 0 
# InputCopy
# 5
# 0
# 2 2 3
# 3 1 3 4
# 2 1 2
# 1 2
# OutputCopy
# 0 0 0 0 0 
# 0 0 1 1 0 
# 0 1 0 1 1 
# 0 1 1 0 0 
# 0 0 1 0 0 