# n = input()
# n = list(map(int, n.split()))
# m = input()
# m = list(map(int, m.split()))

# a = 0
# b = 0
# freq = {}
# max = 0

# while True:
#     if b >= n[0]:
#         break
#     freq[m[b]] = freq.get(m[b], 0) + 1
#     while len(freq) > n[1]:
#         freq[m[a]] -= 1
#         if freq[m[a]] == 0:
#             del freq[m[a]]
#         a += 1
#     max = max(max, b - a + 1)
#     b += 1

# print(max if max > 0 else 0)

par = list(map(int, input().split()))
seq = list(map(int, input().split()))

lft = 0
rgt = 0
lng = 0
cnt = {}

while rgt < par[0]:
    cur = seq[rgt]
    cnt[cur] = cnt.get(cur, 0) + 1
    
    while len(cnt) > par[1]:
        tmp = seq[lft]
        cnt[tmp] -= 1
        if cnt[tmp] == 0:
            del cnt[tmp]
        lft += 1
    
    len_val = rgt - lft + 1
    lng = max(lng, len_val)
    rgt += 1

print(lng)
