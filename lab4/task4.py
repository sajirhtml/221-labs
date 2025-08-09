def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        return
    
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    
    deg = [0] * (n + 1)
    adj = []
    i = 0
    while i <= (n + 1):
        adj.append([])
        i += 1

    
    for i in range(m):
        deg[u[i]] += 1
        deg[v[i]] += 1
        adj[u[i]].append(v[i])
        adj[v[i]].append(u[i])
    
    st = -1
    for i in range(1, n + 1):
        if deg[i] > 0:
            st = i
            break
    
    if st == -1:
        print("YES")
        return
    
    vd = [False] * (n + 1)
    stack = [st]
    vd[st] = True
    
    while stack:
        curr = stack.pop()
        for ch in adj[curr]:
            if not vd[ch]:
                vd[ch] = True
                stack.append(ch)
    
    for i in range(1, n + 1):
        if deg[i] > 0 and not vd[i]:
            print("NO")
            return
    
    oc = 0
    for i in range(1, n + 1):
        if deg[i] % 2 == 1:
            oc += 1
    
    if oc == 0 or oc == 2:
        print("YES")
    else:
        print("NO")

solve()



# D. The Seven Bridges of Königsberg
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an undirected unweighted connected graph with N nodes and M edges. There can be self loop or multiple edges. Your task is to determine whether an Eulerian Path exists in the graph.

# In graph theory, an Eulerian path (also called an Eulerian trail or Eulerian walk) is a path in a graph that visits every edge exactly once and may st and end at different vertices. However, a vertex can be vd multiple times.

# Input
# The first line contains two integers N and M (1≤N≤2×10^5,0≤M≤3×10^5)
#  — the number of vertices and the total number of edges.

# The second line contains M integers u1,u2,u3…um
#  (1≤ui≤N)
#  — where the i-th integer represents the node that is one endpoint of the i-th edge.

# The third line contains M integers v1,v2,v3…vm
#  (1≤vi≤N)
#  — where the i-th integer represents the node that is other endpoint of the i-th edge.

# The i'th edge of this graph is between the i'th node in the second line and the i'th node in the third line.

# Output
# If an Eulerian Path exists, print YES. Otherwise, print NO.

# Examples
# InputCopy
# 5 10
# 5 5 5 2 2 2 3 3 4 2
# 2 3 1 3 4 1 4 1 2 4
# OutputCopy
# YES
# InputCopy
# 5 4
# 1 4 3 2
# 4 3 2 5
# OutputCopy
# YES
# InputCopy
# 8 7
# 4 4 6 6 3 1 8
# 6 5 3 2 7 8 7
# OutputCopy
# NO
# InputCopy
# 7 6
# 3 5 7 6 4 2
# 5 7 6 4 2 1
# OutputCopy
# YES