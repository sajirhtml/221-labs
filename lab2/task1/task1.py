import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = len(arr) - 1

while l < r:
    total = arr[l] + arr[r]
    if total == S:
        print(l + 1, r + 1)
        sys.exit()
    elif total < S:
        l += 1
    else:
        r -= 1

print(-1)




# A. Two Sum Trouble
# time limit per test1 second
# memory limit per test256 megabytes
# Forbidden Keywords for the Quiz: open, file, creat(, fstream, thread, process, system(, exec(

# Your little brother, Bob, loves playing with integers. One day, his teacher gave him a sorted list of N integers in non-decreasing order. Now, your brother wants to play a game with you.

# Bob will give you an integer S. You have to find if it is possible to find two values from the list (at distinct positions) whose sum is equal to S.

# Since you are feeling very tired, you decide to write a program that can quickly answer Bob's query.

# Input
# The first line contains two integers N (1≤N≤106)
#  and S (1≤S≤109)
# , denoting the length of the list, and the target Sum.

# In the next line, there will be N integers a1,a2,a3…an
#  (1≤ai≤109)
#  in non-decreasing order, separated by spaces.

# Output
# Print two distinct 1-based indices i and j such that ai+aj=S
#  where i<j
# . If no such pair exists, then print -1. If multiple solutions exist, you may print any one of the valid answers.

# Examples
# InputCopy
# 4 10
# 1 3 5 7
# OutputCopy
# 2 4
# InputCopy
# 6 18
# 1 5 8 9 9 10
# OutputCopy
# 3 6
# InputCopy
# 4 7
# 2 4 6 8
# OutputCopy
# -1
# InputCopy
# 4 10
# 1 5 6 8
# OutputCopy
# -1
# Note
# In the second sample input, 4 5 is also a valid output.