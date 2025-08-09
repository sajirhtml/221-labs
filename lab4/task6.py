def solve():
    n = int(input())
    x, y = map(int, input().split())
    
    d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    m = []
    
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            m.append((nx, ny))
    
    m.sort()
    print(len(m))
    for a, b in m:
        print(a, b)

solve()




# F. The King of Königsberg
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an N∗N
#  chessboard and the initial position (x,y)
#  of a King piece. The King can move one step in any of the 8 possible directions: Up, Down, Left, Right, Top-left diagonal, Top-right diagonal, Bottom-left diagonal, Bottom-right diagonal.

# Moves of a King in Chess
# Your task is to determine the number of valid moves the King can make in one move. A move is valid if it remains inside the board.

# Input
# The first line contains an integer (1≤N≤2×10^5)
#  — the size of the chessboard.

# The second line contains two integers (1≤x,y≤N)
#  — the initial position of the King on the chessboard.

# Output
# First, print an integer K
#  — the number valid moves the King can make in one move.

# Next, print K
#  lines, each containing two integers representing a valid move in ascending order. A move (a,b)
#  is smaller than (c,d)
#  if a<c
#  or if a=c
#  and b<d
# .

# Examples
# InputCopy
# 8
# 1 1
# OutputCopy
# 3
# 1 2
# 2 1
# 2 2
# InputCopy
# 8
# 1 2
# OutputCopy
# 5
# 1 1
# 1 3
# 2 1
# 2 2
# 2 3
# InputCopy
# 8
# 2 2
# OutputCopy
# 8
# 1 1
# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2
# 3 3