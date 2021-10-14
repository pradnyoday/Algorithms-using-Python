def binary_search(arr, low, high, target):
    if(low > high): return -1
    mid = (low + high) // 2
    if(arr[mid] == target):
        return mid
    elif(arr[mid] > target): 
        return binary_search(arr, low, mid-1, target)
    else: 
        return binary_search(arr, mid + 1, high, target)
        
arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 8
ans = binary_search(arr, 0, n-1, 5)
print(ans)