arr1 = input().split()
arr2 = input().split()

n = [int(x) for x in arr1]
m = [int(x) for x in arr2]

a = 0
b = 0
sum_val = 0
max_val = 0

while True:
    if b >= n[0]:
        break
    
    sum_val += m[b]
    while sum_val > n[1] and a <= b:
        sum_val -= m[a]
        a += 1
    
    max_val = max(max_val, b - a + 1)
    b += 1

print(max_val if max_val > 0 else 0)