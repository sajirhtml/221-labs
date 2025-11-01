# n = input()
# n = list(map(int, n.split()))
# m = input()
# m = list(map(int, m.split()))

# a = 0
# b = 0
# freq = {}
# max = 0

# while True:
#     if b >= n[0]:
#         break
#     freq[m[b]] = freq.get(m[b], 0) + 1
#     while len(freq) > n[1]:
#         freq[m[a]] -= 1
#         if freq[m[a]] == 0:
#             del freq[m[a]]
#         a += 1
#     max = max(max, b - a + 1)
#     b += 1

# print(max if max > 0 else 0)

par = list(map(int, input().split()))
seq = list(map(int, input().split()))

lft = 0
rgt = 0
lng = 0
cnt = {}

while rgt < par[0]:
    cur = seq[rgt]
    cnt[cur] = cnt.get(cur, 0) + 1
    
    while len(cnt) > par[1]:
        tmp = seq[lft]
        cnt[tmp] -= 1
        if cnt[tmp] == 0:
            del cnt[tmp]
        lft += 1
    
    len_val = rgt - lft + 1
    lng = max(lng, len_val)
    rgt += 1

print(lng)




# F. Longest K-Distinct Subarray
# time limit per test1 second
# memory limit per test256 megabytes
# Forbidden Keywords for the Quiz: open, file, creat(, fstream, thread, process, system(, exec(

# You are given an array of integers of length N and an integer K. Your task is to find the length of the longest contiguous subarray that contains at most K distinct elements.

# Input
# The input consists of:

# The first line contains two integers N
#  and K
#  — the size of the array and the maximum number of distinct elements allowed (1≤N≤2×105,1≤K≤N)
# .

# The second line contains N
#  space-separated integers A1
# , A2
# , A2
#  …
#  An
#  — the elements of the array (1≤Ai≤N)
# .

# Output
# Print a single integer — the length of the longest contiguous subarray that contains at most K distinct elements.

# Examples
# InputCopy
# 4 1
# 2 1 2 4
# OutputCopy
# 1
# InputCopy
# 6 2
# 6 6 5 6 1 2
# OutputCopy
# 4
# InputCopy
# 1 1
# 1
# OutputCopy
# 1
# InputCopy
# 2 2
# 1 2
# OutputCopy
# 2