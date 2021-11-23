def merge(arr, left, right):
    i = j = k = 0
    l, r = len(left), len(right)
    while(i < l and j < r):
        if(left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while(i < l):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while(j < r):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr):
    if(len(arr) <= 1): return 
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)

arr = [3, 4, 72, 18, 12, 24, 96, -1, 22, 31, 0, -111]
n = len(arr)
merge_sort(arr)
print(arr)