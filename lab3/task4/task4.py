# M = 10**9 + 7

# def mult(a, b):
#     return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % M,
#              (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % M],
#             [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % M,
#              (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % M]]

# def pow(m, x):
#     res = [[1, 0], [0, 1]]
#     while x:
#         if x & 1:
#             res = mult(res, m)
#         m = mult(m, m)
#         x >>= 1
#     return res

M = 10**9 + 7
def mult(a, b):
    return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % M,
             (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % M],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % M,
             (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % M]]

def pow(m, x):
    res = [[1, 0], [0, 1]]
    while x:
        if x & 1:
            res = mult(res, m)
        m = mult(m, m)
        x >>= 1
    return res

for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    x = int(input())
    res = pow([[a, b], [c, d]], x)
    print(res[0][0], res[0][1])
    print(res[1][0], res[1][1])