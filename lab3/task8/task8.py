def bpr(ino, pos):
    if not ino or not pos:
        return []
    
    roo = pos[-1]
    idx = ino.index(roo)
    
    lin = ino[:idx]
    rin = ino[idx + 1:]
    
    lpo = pos[:len(lin)]
    rpo = pos[len(lin):-1]
    
    pre = [roo]
    pre.extend(bpr(lin, lpo))
    pre.extend(bpr(rin, rpo))
    
    return pre

n = int(input())
ino = list(map(int, input().split()))
pos = list(map(int, input().split()))

pre = bpr(ino, pos)
print(*pre)
