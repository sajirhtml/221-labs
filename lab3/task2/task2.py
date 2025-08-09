# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if a[i] > a[j] * a[j]:
#                 count += 1
    
#     print(count)

# solve()


# import bisect

# def cnt(lst, val):
#     idx = bisect.bisect_right(lst, val)
#     return len(lst) - idx

# def ins(lst, val):
#     bisect.insort_left(lst, val)

# def run():
#     arr = list(map(int, input().split()))
#     stk = []
#     ans = 0

#     for num in arr:
#         ans += cnt(stk, num * num)
#         ins(stk, num)

#     print(ans)

# run()

class Fen:
    def __init__(self, sz):
        self.sz = sz
        self.bit = [0] * (sz + 1)
    
    def upd(self, i, v):
        while i <= self.sz:
            self.bit[i] += v
            i += i & (-i)
    
    def qry(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    
    def rqr(self, l, r):
        if l > r:
            return 0
        return self.qry(r) - self.qry(l - 1)

def slv():
    n = int(input())
    arr = list(map(int, input().split()))
    
    sqr = [x * x for x in arr]
    uni = sorted(set(sqr))
    m = len(uni)
    mp = {v: i + 1 for i, v in enumerate(uni)}
    
    ft = Fen(m)
    ans = 0
    
    for i in range(n - 1, -1, -1):
        l, r = 0, m - 1
        pos = 0
        while l <= r:
            md = (l + r) // 2
            if uni[md] < arr[i]:
                pos = md + 1
                l = md + 1
            else:
                r = md - 1
        
        if pos > 0:
            ans += ft.qry(pos)
        
        ft.upd(mp[sqr[i]], 1)
    
    print(ans)

slv()
