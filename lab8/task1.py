import sys
input=sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
    return size[find(ra)]

n, k = map(int, input().split())
parent = list(range(n+1))
size = [1] * (n+1)

out = []
for i in range(k):
    a, b = map(int, input().split())
    out.append(str(union(a, b)))

print("\n".join(out))






# A. Friendship
# time limit per test1 second
# memory limit per test1024 megabytes
# Study material: http://www.shafaetsplanet.com/?p=763

# There is a group of N
#  people living in a small village. Each person in the village has a unique identity — labeled with an integer value between 1 and N. Initially, the villagers don't have any friends. As time passes, they begin to form friendships.

# In this problem, you will be given information of K
#  friendships. You have to print an integer value that denotes the size of their friend circle.

# Suppose five people are living in the village, labeled 1, 2, 3, 4, and 5. Initially, the size of each friend circle is one, since no friendships have been formed yet. One day, person 1 and person 2 become friends. So, the size of their friend circle becomes two. The next day, person 3 and person 4 become friends, and the size of their friend circle becomes two as well. After a few days, person 1 and person 4 become friends. Now, the size of their combined friend circle becomes four, consisting of persons 1, 2, 3, and 4.

# Input
# The first line contains two integers N
# , K
#  (1≤N,K≤3×105)
#  — the total number of people, total number of friendship created.

# The next K lines contain two integers ai,aj(1≤ai,aj≤N,ai≠aj)
#  — two people become friends.

# Output
# For each friendship formation, output a single integer on a new line representing the size of the friend circle that the two people belong to after becoming friends.

# Examples
# InputCopy
# 8 7
# 2 4
# 4 5
# 3 6
# 4 7
# 3 1
# 2 7
# 6 2
# OutputCopy
# 2
# 3
# 2
# 4
# 3
# 4
# 7
# InputCopy
# 6 5
# 4 6
# 2 6
# 1 6
# 1 4
# 1 2
# OutputCopy
# 2
# 3
# 4
# 4
# 4
# InputCopy
# 2 1
# 1 2
# OutputCopy
# 2
# InputCopy
# 5 7
# 4 5
# 3 5
# 3 4
# 2 5
# 2 3
# 1 5
# 1 4
# OutputCopy
# 2
# 3
# 3
# 4
# 4
# 5
# 5
# Note
# In input sample 1,

# Initially, 8 people in the village do not know each other.

# {1} {2} {3} {4} {5} {6} {7} {8}

# — After person 2 and person 4 become friends:

# {1} {2,4} {3} {5} {6} {7} {8}

# The output is 2, since the size of the friends circle {2,4} is 2.

# — After person 4 and person 5 become friends:

# {1} {2,4,5} {3} {6} {7} {8}

# The output is 3, since the size of the friends circle {2,4,5} is 3.

# — After person 3 and person 6 become friends:

# {1} {2,4,5} {3,6} {7} {8}

# The output is 2, since the size of the friends circle {3,6} is 2.

# — After person 4 and person 7 become friends:

# {1} {2,4,5,7} {3,6} {8}

# The output is 4, since the size of the friends circle {2,4,5,7} is 4.

# — After person 3 and person 1 become friends:

# {2,4,5,7} {1,3,6} {8}

# The output is 3, since the size of the friends circle {1,3,6} is 3.

# Since person 2 and person 7 are already in the same friend circle, nothing changes:

# {2,4,5,7} {1,3,6} {8}

# The output is 4, since the size of the friends circle {2,4,5,7} is 4.

# — After person 6 and person 2 become friends:

# {2,4,5,7,1,3,6} {8}

# The output is 7, since the size of the friends circle {2,4,5,7,1,3,6} is 7.