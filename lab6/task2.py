import sys
from collections import deque

def solve():
    inp = sys.stdin.readline
    n, m = map(int, inp().split())
    g = [[] for i in range(n+1)]
    for i in range(m):
        u, v = map(int, inp().split())
        g[u].append(v)
        g[v].append(u)
    vis = [0]*(n+1)
    col = [-1]*(n+1)
    ans = 0
    for i in range(1, n+1):
        if not vis[i]:
            q = deque([i])
            vis[i] = 1
            col[i] = 0
            c0 = 1
            c1 = 0
            while q:
                u = q.popleft()
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = 1
                        col[v] = 1 - col[u]
                        if col[v] == 0:
                            c0 += 1
                        else:
                            c1 += 1
                        q.append(v)
            if c0 > c1:
                ans += c0
            else:
                ans += c1
    print(ans)
solve()





# B. A Football Match
# time limit per test2 seconds
# memory limit per test1024 megabytes
# There is an intense football match going on between Robots and Humans. However, things aren't as simple as they seem — the Robots have disguised themselves to look exactly like Humans! From the outside, it's impossible to tell who is a Robot and who is a Human.

# The audience know only one important information — the Robots tackles only the Humans, and the Humans tackles only the Robots.

# Now, you are given a list of tackles, each involving two players. Based on this information, find the maximum possible number of Robots or Humans.

# Input
# The first line contains two integers N
#  and M
#  (1≤N≤2×10^5,1≤M≤3×10^5)
#  — the number of players in the match and the number of tackles occurred during the match respectively.

# The next M
#  lines will contain two integers ui,vi(1≤ui,vi≤N)
#  — player ui
#  tackled player vi
# . Each tackle between two players will be reported at most once.

# Output
# Print the maximum possible number of Robots or Humans.

# Examples
# InputCopy
# 5 6
# 3 4
# 3 2
# 5 4
# 5 2
# 4 1
# 1 2
# OutputCopy
# 3
# InputCopy
# 5 4
# 4 3
# 1 3
# 3 2
# 3 5
# OutputCopy
# 4
# InputCopy
# 4 1
# 1 3
# OutputCopy
# 3
# InputCopy
# 6 6
# 1 3
# 1 4
# 3 6
# 4 6
# 4 5
# 6 2
# OutputCopy
# 3