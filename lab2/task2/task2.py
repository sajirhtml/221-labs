n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = m - 1
I, J = 1, 1
flag = float('inf')

while i < n and j >= 0:
    sum = a[i] + b[j]
    diff = abs(sum - k)
    
    if diff < flag:
        flag = diff
        I = i + 1
        J = j + 1
    
    if sum == k:
        print(i + 1, j + 1)
        exit()
    
    if sum < k:
        i += 1
    else:
        j -= 1

print(I, J)