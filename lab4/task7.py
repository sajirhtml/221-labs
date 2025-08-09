def solve():
    import sys
    input = sys.stdin.readline
    
    n, m, K = map(int, input().split())
    k = set()
    
    for i in range(K):
        x, y = map(int, input().split())
        k.add((x, y))
    
    ms = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    for x, y in k:
        for dx, dy in ms:
            nx, ny = x + dx, y + dy
            if (nx, ny) in k:
                print("YES")
                return
    
    print("NO")

solve()





# G. The Knights of Königsberg
# time limit per test1 second
# memory limit per test256 megabytes
# You are given a chessboard of size N×M
# . There are K
#  knights placed on distinct cells of this board. The standard movement of a knight in chess is as follows: it ms in an "L" shape—either two squares in one direction and then one square perpendicular to that, or one square in one direction and then two squares perpendicular to that. A knight can jump over other pieces.


# Your task is to determine whether any pair of knights are attacking each other. If at least one pair of knights are in positions such that one can attack the other in a single move, print "YES". Otherwise, print "NO".

# Input
# The first line contains three integers N
# , M
# , and K
#  (1≤N,M≤1000
# , 0≤K≤10^5
# ) — the number of rows, the number of columns, and the number of knights on the board.

# Each of the next K
#  lines contains two integers xi
# , yi
#  (1≤xi≤N
# , 1≤yi≤M
# ) — the position of the i
# -th knight on the board.

# It is guaranteed that all K
#  knights are placed on distinct positions.

# Examples
# InputCopy
# 6 4 4
# 2 3
# 4 2
# 1 2
# 3 3
# OutputCopy
# YES
# InputCopy
# 4 4 4
# 1 1
# 1 3
# 2 2
# 2 4
# OutputCopy
# NO