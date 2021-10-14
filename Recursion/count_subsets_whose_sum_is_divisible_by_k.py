def print_subsets(i, s, arr, n, k):
    if(i == n):
        if(s % k == 0):
            return 1
        return 0
    s += arr[i]
    l = print_subsets(i+1, s, arr, n, k)
    s -= arr[i]
    r = print_subsets(i+1, s, arr, n, k)
    return l + r
arr = [4, 3, 2]
n = 3
k = 3
ans = print_subsets(0, 0, arr, n, k) - 1
print(ans)