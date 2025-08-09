# def pm(bs, exp, mod):
#     res = 1
#     bs %= mod
#     while exp > 0:
#         if exp & 1:
#             res = res * bs % mod
#         bs = bs * bs % mod
#         exp >>= 1
#     return res

# def modI(a, m):
#     def gcd(a, b):
#         if not a:
#             return b, 0, 1
#         g, x1, y1 = gcd(b % a, a)
#         return g, y1 - b // a * x1, x1
    
#     g, x, _ = gcd(a % m, m)
#     return (x % m + m) % m if g == 1 else 0

# def gSum(a, n, m):
#     a %= m
#     if a == 0: return 0
#     if a == 1: return n % m
    
#     a_n = pm(a, n, m)
#     num = (a_n - 1 + m) % m
#     den = (a - 1 + m) % m
    
#     return a * num % m * modI(den, m) % m

# t = int(input())
# for _ in range(t):
#     a, n, m = map(int, input().split())
#     print(gSum(a, n, m))

# def mpw(b, e, m):
#     r = 1
#     b %= m
#     while e > 0:
#         if e & 1:
#             r = (r * b) % m
#         e >>= 1
#         b = (b * b) % m
#     return r

# def miv(a, m):
#     return mpw(a, m - 2, m)

# def sgs(a, n, m):
#     a %= m
#     if a == 1:
#         return n % m
#     if a == 0:
#         return 0
#     apn = mpw(a, n, m)
#     num = (apn - 1 + m) % m
#     den = (a - 1 + m) % m
#     inv = miv(den, m)
#     return (a * num % m * inv) % m

# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     a, n, m = map(int, input().split())
#     print(sgs(a, n, m))

# import sys
# input = sys.stdin.readline

# def mex(b, e, m):
#     r = 1
#     b %= m
#     while e > 0:
#         if e & 1:
#             r = (r * b) % m
#         b = (b * b) % m
#         e >>= 1
#     return r

# def miv(a, m):
#     return mex(a, m - 2, m)

# from math import gcd

# T = int(input())
# for _ in range(T):
#     a, n, m = map(int, input().split())
#     if a == 1:
#         print(n % m)
#         continue
#     if gcd(a - 1, m) != 1:
#         print(-1)
#         continue
#     pn = mex(a, n, m)
#     iv = miv(a - 1, m)
#     ans = (a * (pn - 1)) % m
#     ans = (ans * iv) % m
#     print(ans)


