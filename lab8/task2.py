import sys
input=sys.stdin.readline

n,m=map(int,input().split())
e=[]
for i in range(m):
    u,v,w=map(int,input().split())
    e.append((w,u,v))
e.sort()
p=list(range(n+1))
r=[0]*(n+1)
def f(x):
    while p[x]!=x:
        p[x]=p[p[x]]
        x=p[x]
    return x
def u(a,b):
    ra,rb=f(a),f(b)
    if ra==rb:return 0
    if r[ra]<r[rb]:
        p[ra]=rb
    elif r[ra]>r[rb]:
        p[rb]=ra
    else:
        p[rb]=ra
        r[ra]+=1
    return 1
ans=0
for w,a,b in e:
    if u(a,b):
        ans+=w
print(ans)





# B. Help the King!
# time limit per test1 second
# memory limit per test1024 megabytes
# In the kingdom of Beluga, there are N
#  cities connected by M
#  bidirectional roads. Each road has a maintenance cost. There is at least one way to travel between any two cities.

# The king is worried about the growing cost of maintaining all these roads. To fix this, he asks his advisors for help.

# The council suggests keeping only the roads needed to connect all the cities with the least total maintenance cost. Instead of building new roads, the king decides to save money by removing some of the existing ones.

# Since you're known for your programming skills, the king calls on you. He wants you to figure out the minimum total maintenance cost that can be achieved by removing some roads—while still making sure that all the cities remain connected.

# Input
# The first line contains two integers N,M(2≤N≤2×105,1≤M≤3×105)
#  — the number of vertices, total number of edges.

# The next M
#  lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤106)
#  — there is an edge between the node ui
#  and the node vi
#  with a maintenance cost wi
# .

# Output
# The output should contain a single integer, with the minimum total maintenance cost achievable.

# Examples
# InputCopy
# 4 3
# 3 4 5
# 3 1 5
# 2 1 2
# OutputCopy
# 12
# InputCopy
# 6 5
# 2 6 3
# 2 3 3
# 2 1 4
# 6 5 1
# 5 4 2
# OutputCopy
# 13
# InputCopy
# 2 1
# 1 2 9
# OutputCopy
# 9
# InputCopy
# 5 7
# 1 2 8
# 1 4 3
# 1 5 4
# 2 4 8
# 2 3 5
# 4 3 4
# 3 5 5
# OutputCopy
# 16