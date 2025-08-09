N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

adj = []
for i in range(N + 1):
    adj.append([])

for j in range(M):
    adj[u[j]].append((v[j], w[j]))

for n in range(1, N + 1):
    l = []
    for ds, w in adj[n]:
        l.append(f"({ds},{w})")
    p = ' '.join(l)
    print(f"{n}: {p}")


# B. Adjacency List Representation
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a directed wed graph with N nodes and M edges. The nodes are numbered from 1 to N. Each edge represents a direct connection between two nodes. There is no self loop or multi edge.

# Input
# The first line contains two integers N and M (1≤N≤100,0≤M≤N(N−1)/2)
#  — the number of vertices and the total number of edges.

# The second line contains M integers u1,u2,u3…um
#  (1≤ui≤N)
#  — where the i-th integer represents the node that is one endpoint of the i-th edge.

# The third line contains M integers v1,v2,v3…vm
#  (1≤vi≤N)
#  — where the i-th integer represents the node that is other endpoint of the i-th edge.

# Thr fourth line contains M integers w1,w2,w3…wm
#  (1≤wi≤1000)
#  — where the i-th integer represents the w of the i-th edge.

# The i'th edge of this graph is from the i'th node in the second line to the i'th node in the third line, their w is the i'th value in the fourth line.

# Output
# For the given input, the output should be the Adjacency List representation of the graph as shown in the sample output.

# Examples
# InputCopy
# 4 5
# 4 1 4 3 3
# 3 2 2 2 1
# 4 4 10 8 5
# OutputCopy
# 1: (2,4)
# 2:
# 3: (2,8) (1,5)
# 4: (3,4) (2,10)
# InputCopy
# 4 4
# 3 3 2 4
# 2 1 1 3
# 9 5 8 10
# OutputCopy
# 1:
# 2: (1,8)
# 3: (2,9) (1,5)
# 4: (3,10)