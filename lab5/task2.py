import sys
sys.setrecursionlimit(2*100000+5)

n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = u[i], v[i]
    g[a].append(b)
    g[b].append(a)

for i in range(1, n + 1):
    g[i].sort()

vis = [0] * (n + 1)
res = []
st = [1]

while st:
    x = st[-1]
    if not vis[x]:
        vis[x] = 1
        res.append(x)
    
    found = 0
    for y in g[x]:
        if not vis[y]:
            st.append(y)
            found = 1
            break
    
    if not found:
        st.pop()

print(' '.join(map(str, res)))






# B. Can you Traverse-2?
# time limit per test1 second
# memory limit per test1024 megabytes
# You are given an undirected unweighted graph with N cities and M roads. The cities are numbered from 1
#  to N
# . The graph is connected, and contains no self-loops or multiple edges.

# Your task is to perform a Depth-First Search (DFS) starting from node 1
#  and print the order in which the nodes are visited.

# Pseudocode of DFS

# The depth-first-search procedure below assumes that the input graph G = (V, E) is represented using adjacency lists.

# colourInitializing(G):
#    for each vertex u in G.V:
#       u.colour = 0

# DFS(G,u):
#    u.colour = 1
#    for each v in G.Adj[u]:
#       if v.colour == 0:
#          DFS(G,v)
# Important Notes for Python Language

# Python has a default recursion limit (usually around 1000) to prevent stack overflow from runaway recursion. As a result, if you are using recursion to solve a problem, you must increase the recursion limit manually.

# How to Increase the Recursion Depth—
# import sys
# sys.setrecursionlimit(#set_the_value)
# What Value to Set— Setting the recursion depth too high can cause a stack overflow or crash your program. This happens because each recursive call uses stack memory, and the system allocates only a limited amount of memory for the stack. If the recursion goes deeper than the system can handle, it may lead to a segmentation fault. Check what the maximum recursion depth might be in your problem. In this problem, the maximum number of nodes the input graph can have is 2×10^5
# , so we set the limit accordingly. We add a small buffer (+5, or sometimes +10, +50, etc.) to avoid edge-case runtime errors.
# import sys
# sys.setrecursionlimit(2*100000+5)
# Choose Python over PyPy to Avoid MLE/RTE— While PyPy is generally faster due to Just-In-Time (JIT) compilation, it also uses more memory. In recursion-heavy problems, PyPy may consume significantly more stack memory per call compared to CPython. This can lead to Memory Limit Exceeded (MLE) errors on some platforms, especially when recursion depth is high. Therefore, for problems that involve deep recursion and strict memory constraints, it is safer to submit your solution using Python (CPython) rather than PyPy.
# Input
# The first line contains two integers N
#  and M
#  (1≤N≤2×10^5,1≤M≤3×10^5)
#  — the number of cities and the total number of roads.

# The second line contains M
#  integers u1,u2,u3…um
#  (1≤ui≤N)
#  — where the i-th integer represents the node that is one endpoint of the i-th edge.

# The third line contains M
#  integers v1,v2,v3…vm
#  (1≤vi≤N)
#  — where the i-th integer represents the node that is other endpoint of the i-th edge.

# The i-th edge of this graph is between the i-th node in the second line and the i-th node in the third line.

# Output
# Print the DFS traversal starting from node 1
#  as a space-separated list of visited nodes. If there are multiple DFS path traversal order, you may print any.

# Examples
# InputCopy
# 4 3
# 1 3 1
# 4 2 3
# OutputCopy
# 1 3 2 4 
# InputCopy
# 6 8
# 1 5 3 4 6 1 6 4
# 5 3 4 6 2 3 3 1
# OutputCopy
# 1 3 4 6 2 5 
# InputCopy
# 5 7
# 5 1 3 2 4 4 4
# 1 3 2 4 1 3 5
# OutputCopy
# 1 3 2 4 5 
# Note
# In the first Sample Input, the graph looks like this:



# There are two valid paths that follow the DFS order: 1 4 3 2
#  and 1 3 2 4
# . You may print either one of these paths in the output.