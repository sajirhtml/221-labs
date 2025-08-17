import sys
input = sys.stdin.readline

n, r = map(int, input().split())
g = [[] for i in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

sz = [0] * (n+1)
st = [(r, -1, 0)]

while st:
    u, p, s = st.pop()
    if s == 0:
        st.append((u, p, 1))
        for v in g[u]:
            if v != p:
                st.append((v, u, 0))
    else:
        sz[u] = 1
        for v in g[u]:
            if v != p:
                sz[u] += sz[v]

q = int(input())
for i in range(q):
    x = int(input())
    print(sz[x])



#     E. Easy Tree Queries
# time limit per test1 second
# memory limit per test1024 megabytes
# There is a tree with N nodes. The tree is rooted at a given node R.

# You will be given Q queries. In each query, you are asked to find the size of the subtree of a given node X.

# Input
# The first line contains two integers N
# , R
#  (1≤N≤2×10^5,1≤R≤N)
#  — the number of nodes and the root of the tree.

# The next N−1
#  lines each contain two integers ui,vi(1≤ui,vi≤N)
#  — representing an bidirectional edge between nodes ui
#  and vi
# .

# The next line contains an integer Q(1≤Q≤2×10^5)
#  — the number of queries.

# The next Q
#  lines each contain a single integer X(1≤X≤N)
#  — the node whose subtree size you need to compute.

# Output
# For each query, print a single integer — the size of the subtree of node X
# .

# Examples
# InputCopy
# 4 1
# 3 1
# 1 2
# 4 2
# 3
# 1
# 4
# 2
# OutputCopy
# 4
# 1
# 2
# InputCopy
# 5 3
# 1 2
# 5 3
# 3 2
# 2 4
# 5
# 3
# 5
# 4
# 2
# 1
# OutputCopy
# 5
# 1
# 1
# 3
# 1
# InputCopy
# 8 2
# 1 7
# 7 3
# 3 6
# 6 5
# 5 2
# 2 8
# 8 4
# 8
# 6
# 4
# 2
# 1
# 7
# 5
# 8
# 3
# OutputCopy
# 4
# 1
# 8
# 1
# 2
# 5
# 2
# 3
# InputCopy
# 1 1
# 1
# 1
# OutputCopy
# 1