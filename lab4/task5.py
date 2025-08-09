n, m = map(int, input().split())

if m == 0:
    print(' '.join(['0'] * n))
else:
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    
    id = [0] * (n + 1)
    od = [0] * (n + 1)
    
    for i in range(m):
        od[u[i]] += 1
        id[v[i]] += 1
    
    r = []
    for i in range(1, n + 1):
        r.append(str(id[i] - od[i]))
    
    print(' '.join(r))




#     E. Edge Queries
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a directed unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Your task is to find the difference of indegree and outdegree of each node in the graph.

# Input
# The first line contains two integers N and M (1≤N≤2×105,0≤M≤3×105)
#  — the number of vertices and the total number of edges.

# The second line contains M integers u1,u2,u3…um
#  (1≤ui≤N)
#  — where the i-th integer represents the node that is one endpoint of the i-th edge.

# The third line contains M integers v1,v2,v3…vm
#  (1≤vi≤N)
#  — where the i-th integer represents the node that is other endpoint of the i-th edge.

# The i-th edge of this graph is from the i-th node in the second line to the i-th node in the third line.

# Output
# Output a single line with N space-separated integers, where the i-th integer is the difference of indegree and outdegree of node i.

# Examples
# InputCopy
# 5 10
# 2 5 4 3 2 4 3 4 1 3
# 5 1 5 5 1 2 2 1 3 4
# OutputCopy
# 2 0 -2 -2 2
# InputCopy
# 5 4
# 5 3 3 2
# 1 1 2 4
# OutputCopy
# 2 0 -2 1 -1
# InputCopy
# 8 7
# 7 7 7 2 1 4 1
# 2 6 3 4 2 8 5
# OutputCopy
# -2 1 1 0 1 1 -3 1