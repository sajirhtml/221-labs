import sys, heapq
def solve():
    n=int(sys.stdin.readline())
    w=[]
    for i in range(n):
        w.append(sys.stdin.readline().strip())
    g=[]
    for i in range(26):
        g.append(set())
    d=[0]*26
    u=[False]*26
    for i in range(n-1):
        a=w[i]
        b=w[i+1]
        m=min(len(a),len(b))
        f=0
        for j in range(m):
            if a[j]!=b[j]:
                x=ord(a[j])-97
                y=ord(b[j])-97
                if y not in g[x]:
                    g[x].add(y)
                    d[y]+=1
                f=1
                break
        if not f and len(a)>len(b):
            print(-1)
            return
    for i in range(n):
        for c in w[i]:
            u[ord(c)-97]=1
    h=[]
    for i in range(26):
        if u[i] and d[i]==0:
            heapq.heappush(h,i)
    res=[]
    while h:
        x=heapq.heappop(h)
        res.append(chr(x+97))
        for y in g[x]:
            d[y]-=1
            if d[y]==0:
                heapq.heappush(h,y)
    if len(res)!=sum(u):
        print(-1)
    else:
        print(''.join(res))
solve()




# E. An Ancient Ordering
# time limit per test1 second
# memory limit per test256 megabytes
# You have found an old dictionary containing N words. The words are stored in an order that is different from the regular Latin lexicographic order.

# Your task is to determine the order of the alphabet that satisfies the lexicographic order of this dictionary. If there are multiple valid orders, print the lexicographically smallest one. For example, the sequence S1=′′d x i k′′
#  is lexicographically smaller than the sequence S2=′′d x p a k′′
# .

# If no such valid sequence exists, print −1
# . A valid ordering is not possible if the characters create cyclic dependencies or if a longer word appears before a shorter word that is a prefix of it.

# Input
# The first line contains an integer N
#  (1≤N≤1000)
#  — the number of words in the dictionary.

# The next N
#  line contains a string S
#  (1≤|S|≤100)
# . Each word consists of only lowercase Latin letters a−z
# .

# Output
# Find out the order of the alphabets that satisfy the sorting order of the words in the given dictionary. If there are multiple valid orders, print the lexicographically smallest one. If no such valid sequence exists, print −1
# .

# Examples
# InputCopy
# 3
# eat
# tea
# ate
# OutputCopy
# eta
# InputCopy
# 9
# error
# tooth
# tot
# teeth
# their
# there
# thi
# tie
# hit
# OutputCopy
# oethir
# InputCopy
# 6
# gef
# gie
# hf
# hd
# hc
# ha
# OutputCopy
# efdcaghi
# InputCopy
# 5
# cmwaqe
# yent
# jtdgx
# wlp
# xufjpf
# OutputCopy
# acdefglmnpqtuyjwx
# InputCopy
# 6
# abc
# ab
# p
# pq
# pqr
# pqrs
# OutputCopy
# -1
# InputCopy
# 2
# pigeon
# pigeons
# OutputCopy
# eginops
# InputCopy
# 4
# ab
# bc
# ca
# ac
# OutputCopy
# -1