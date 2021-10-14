def print_subsets(i, ans, s, arr, n, k):
    if(i == n):
        if(s % k == 0):
            print(ans)
        return
    ans.append(arr[i]) # Pick item
    s += arr[i]
    print_subsets(i+1, ans, s, arr, n, k)
    ans.pop() # Dont Pick item
    s -= arr[i]
    print_subsets(i+1, ans, s, arr, n, k)
arr = [4, 3, 2]
n = 3
k = 3
print_subsets(0, [], 0, arr, n, k)