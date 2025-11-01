# import sys

# arr1 = input().split()
# arr2 = input().split()

# n = int(arr1[0])
# x = int(arr1[1])

# for i in range(n):
#     a = x - int(arr2[i])
#     map = {}
#     for j in range(i+1, n):
#         b = a - int(arr2[j])
#         if b in map:
#             k = map[b]
#             print((i + 1), (j + 1), (k + 1))
#             sys.exit()
#         map[int(arr2[j])] = j

# print(-1)

# n = input()
# n = list(map(int, n.split()))
# arr = input()
# arr = list(map(int, arr.split()))
# paired = list(map(lambda x: (x[1], x[0] + 1), enumerate(arr)))
# paired.sort() 

# i = 0
# found = False

# while True:
#     if i >= n[0] - 2:
#         break

#     target = n[1] - paired[i][0]
#     p1 = i + 1
#     p2 = n[0] - 1

#     while True:
#         if p1 >= p2:
#             break

#         total = paired[p1][0] + paired[p2][0]
#         if total == target:
#             print(paired[i][1], paired[p1][1], paired[p2][1])
#             found = True
#             break
#         elif total < target:
#             p1 += 1
#         else:
#             p2 -= 1

#     if found:
#         break
#     i += 1

# if not found:
#     print(-1)


n, x = map(int, input().split())
a = list(map(int, input().split()))

arr = [(a[i], i + 1) for i in range(n)]
arr.sort()

for i in range(n):
    target = x - arr[i][0]
    l, r = 0, n - 1
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        s = arr[l][0] + arr[r][0]
        if s == target:
            print(arr[i][1], arr[l][1], arr[r][1])
            exit()
        elif s < target:
            l += 1
        else:
            r -= 1

print(-1)


# C. Triple The Trouble
# time limit per test1 second
# memory limit per test256 megabytes
# Forbidden Keywords for the Quiz: open, file, creat(, fstream, thread, process, system(, exec(

# You are given an array of n
#  integers, and your task is to find three values (at distinct positions) whose sum is x
# .

# Input
# The first input line has two integers n
#  (1≤n≤5000)
#  and x
#  (1≤x≤109)
# , the array size and the target sum. The second line has n
#  integers a1,a2,…,an
#  (1≤ai≤109)
# , the array values.

# Output
# Print three integers: the positions of the values. If there are several solutions, you may print any of them. If there are no solutions, print -1.

# Examples
# InputCopy
# 7 3
# 2 1 1 2 2 1 1
# OutputCopy
# 2 3 6 
# InputCopy
# 3 5
# 1 3 2
# OutputCopy
# -1