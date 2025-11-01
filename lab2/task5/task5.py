# n= list(map(int, input().split()))
# m= list(map(int, input().split()))

arr1 = input().split()
arr2 = input().split()

n = [int(x) for x in arr1]
m = [int(x) for x in arr2]

a = 0
b = 0
sum = 0
max = 0

while True:
    if b >= n[0]:
        break
    
    sum += m[b]
    while sum > n[1] and a <= b:
        sum -= m[a]
        a += 1
    
    max = max(max, b - a + 1)
    b += 1

print(max if max > 0 else 0)





# E. Longest Subarray Sum
# time limit per test1 second
# memory limit per test256 megabytes
# Forbidden Keywords for the Quiz: open, file, creat(, fstream, thread, process, system(, exec(

# You are given an array of N integers and an integer K. Your task is to find the length of the longest contiguous subarray whose sum is less than or equal to K.

# Input
# The first line contains two integers N (1≤N≤105)
#  and K (1≤K≤109)
#  — the size of the array and the maximum allowed sum.

# The second line contains N space-separated integers a1,a2,a3…an
#  (1≤ai≤106)
#  — the elements of the array.

# Output
# Print a single integer — the length of the longest contiguous subarray whose sum is less than or equal to K.

# Examples
# InputCopy
# 5 4
# 4 1 2 1 5
# OutputCopy
# 3
# InputCopy
# 5 5
# 1 1 1 1 1
# OutputCopy
# 5
# InputCopy
# 3 1
# 2 3 4
# OutputCopy
# 0
# InputCopy
# 10 12
# 1 2 6 4 3 2 3 1 4 2
# OutputCopy
# 5
# Note
# In the first example, possible subarrays with sum less than or equal to 4 are [4],[1],[2],[1],[1,2],[2,1],[1,2,1]
# . Among them, the longest size is 3.

# In the second example, sum of the entire array is 5. Hence, we can take the whole array.

# In the third example, no subarray has sum less than or equal to 1. Hence, the answer is 0.