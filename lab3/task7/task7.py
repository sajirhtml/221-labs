def bpo(ino, pre):
    if not ino or not pre:
        return []
    
    roo = pre[0]
    idx = ino.index(roo)
    
    lin = ino[:idx]
    rin = ino[idx + 1:]
    
    lpr = pre[1:1 + len(lin)]
    rpr = pre[1 + len(lin):]
    
    lpo = bpo(lin, lpr)
    rpo = bpo(rin, rpr)
    
    return lpo + rpo + [roo]

n = int(input())
ino = list(map(int, input().split()))
pre = list(map(int, input().split()))

pos = bpo(ino, pre)
print(*pos)
