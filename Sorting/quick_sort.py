def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if(arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if(len(arr) <= 1): return
    if(low < high):
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

arr = [3, 4, 72, 18, 12, 24, 96, -1, 22, 31, 0, -111]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)