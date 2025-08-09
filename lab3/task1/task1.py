def merge(a, b):
    m = []
    inv = 0
    i, j = 0, 0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            m.append(a[i])
            i += 1
        else:
            inv += len(a) - i
            m.append(b[j])
            j += 1
    
    while i < len(a):
        m.append(a[i])
        i += 1
    
    while j < len(b):
        m.append(b[j])
        j += 1
    
    return m, inv

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        a1, inv1 = mergeSort(arr[:mid])
        a2, inv2 = mergeSort(arr[mid:])
        m, inv3 = merge(a1, a2)
        return m, inv1 + inv2 + inv3

n = int(input())
arr = list(map(int, input().split()))
sArr, invC = mergeSort(arr)
print(invC)
print(' '.join(map(str, sArr)))