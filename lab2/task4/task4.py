a = 0
b = 0
arr = []
N = int(input())
n = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))

while True:
        if a >= N or b >= M: break
        elif m[b] < n[a]:
            arr.append(m[b])
            b += 1
        elif n[a] < m[b]:
            arr.append(n[a])
            a += 1
        else:
            arr.append(n[a])
            a += 1

while a < N:
    arr.append(n[a])
    a += 1

while b < M:
    arr.append(m[b])
    b += 1

print(*arr)



# D. A Beautiful Sorted List
# time limit per test1 second
# memory limit per test1024 megabytes
# Forbidden Keywords for the Quiz: sort, open, file, creat(, fstream, thread, process, system(, exec(

# Alice and Bob are two friends. Alice has a list of length N in non-decreasing order, and Bob has a list of length M, also in non-decreasing order.

# Now, they want to combine their lists into a single non-decreasing list of length N+M. However, they are not very good at algorithms, so they asked for your help.

# Since you are a computer science student, your task is to write an efficient algorithm to merge the two given lists into one non-decreasing list. Solve the problem in O(N+M).

# Input
# The first line contains an integer N (1≤N≤106)
# , denoting the length of Alice's list.

# The second line contains N space-separated integers representing Alice's list.

# The third line contains an integer M (1≤M≤106)
# , denoting the length of Bob's list.

# The fourth line contains M space-separated integers representing Bob's list.

# All the numbers given in the input will fit within a 32-bit signed integer. It is guaranteed that the given lists will be in non-decreasing order.

# Output
# You have to make a sorted list in non-decreasing order from the given lists and show the output.

# Examples
# InputCopy
# 4
# 1 3 5 7
# 4
# 2 2 4 8
# OutputCopy
# 1 2 2 3 4 5 7 8 
# InputCopy
# 3
# 2 10 12
# 6
# 3 4 6 7 8 9
# OutputCopy
# 2 3 4 6 7 8 9 10 12 
# InputCopy
# 5
# 1 2 3 4 5
# 2
# 10 12
# OutputCopy
# 1 2 3 4 5 10 12 
# InputCopy
# 4
# 1 2 12 13
# 3
# 10 15 18
# OutputCopy
# 1 2 10 12 13 15 18 
# InputCopy
# 8
# 1 2 3 8 8 10 12 14
# 9
# 1 1 4 5 6 8 13 15 16
# OutputCopy
# 1 1 1 2 3 4 5 6 8 8 8 10 12 13 14 15 16 