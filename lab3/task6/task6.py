def opt(arr):
    res = []
    def bld(lft, rgt):
        if lft > rgt:
            return
        mid = (lft + rgt) // 2
        res.append(arr[mid])
        bld(lft, mid - 1)
        bld(mid + 1, rgt)
    bld(0, len(arr) - 1)
    return res

n = int(input())
arr = list(map(int, input().split()))
ord = opt(arr)
print(*ord)
