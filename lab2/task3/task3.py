# import sys

# arr1 = input().split()
# arr2 = input().split()

# n = int(arr1[0])
# x = int(arr1[1])

# for i in range(n):
#     a = x - int(arr2[i])
#     map = {}
#     for j in range(i+1, n):
#         b = a - int(arr2[j])
#         if b in map:
#             k = map[b]
#             print((i + 1), (j + 1), (k + 1))
#             sys.exit()
#         map[int(arr2[j])] = j

# print(-1)

n = input()
n = list(map(int, n.split()))
arr = input()
arr = list(map(int, arr.split()))
paired = list(map(lambda x: (x[1], x[0] + 1), enumerate(arr)))
paired.sort() 

i = 0
found = False

while True:
    if i >= n[0] - 2:
        break

    target = n[1] - paired[i][0]
    p1 = i + 1
    p2 = n[0] - 1

    while True:
        if p1 >= p2:
            break

        total = paired[p1][0] + paired[p2][0]
        if total == target:
            print(paired[i][1], paired[p1][1], paired[p2][1])
            found = True
            break
        elif total < target:
            p1 += 1
        else:
            p2 -= 1

    if found:
        break
    i += 1

if not found:
    print(-1)