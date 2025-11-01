n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = m - 1
I, J = 1, 1
flag = float('inf')

while i < n and j >= 0:
    sum = a[i] + b[j]
    diff = abs(sum - k)
    
    if diff < flag:
        flag = diff
        I = i + 1
        J = j + 1
    
    if sum == k:
        print(i + 1, j + 1)
        exit()
    
    if sum < k:
        i += 1
    else:
        j -= 1

print(I, J)




# B. Two Sum Revisited
# time limit per test1 second
# memory limit per test256 megabytes
# Forbidden Keywords for the Quiz: open, file, creat(, fstream, thread, process, system(, exec(

# You are given two integer arrays A
#  and B
#  of sizes N
#  and M
# , respectively, and an integer K
# . Both arrays are sorted in non-decreasing order. Your task is to find any pair of indices (i,j)
#  such that:

# i
#  is a valid index in array A
#  (1≤i≤N)
# j
#  is a valid index in array B
#  (1≤j≤M)
# the sum A[i] + B[j] is closest to K (i.e., it minimizes |A[i] + B[j] − K|).
# Input
# The first line contains Three integers N
# , M
#  and K
#  (1≤N,M≤2×105,−109≤K≤109)
# .

# The second line contains N
#  integers — the elements of array A
#  (−109≤Ai≤109)
# .

# The third line contains M
#  integers — the elements of array B
#  (−109≤Bj≤109)
# .

# Output
# Print two space-separated integers i
#  and j
#  the 1-based indices of the chosen pair.

# If there are multiple answers, output any.

# Examples
# InputCopy
# 4 4 0
# -5 -2 -1 5
# -5 0 1 1
# OutputCopy
# 3 4
# InputCopy
# 6 6 1
# -5 -3 3 4 4 5
# -2 0 2 2 3 5
# OutputCopy
# 3 1
# InputCopy
# 1 1 8
# -2
# -8
# OutputCopy
# 1 1
# InputCopy
# 2 2 -4
# -7 4
# -5 4
# OutputCopy
# 1 2
# InputCopy
# 3 4 -2
# -15 -15 8
# -14 4 4 6
# OutputCopy
# 3 1