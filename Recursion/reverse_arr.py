arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def rev(l, r):
    if(l > r): return
    arr[l], arr[r] = arr[r], arr[l]
    return rev(l+1, r - 1)
print(arr)
rev(0, len(arr)-1)
print(arr)