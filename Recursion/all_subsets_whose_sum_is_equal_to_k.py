def print_subsets(i, arr, ans, s, n, k):
    if(i == n): 
        if(s == k):
            print(ans)
            return
        return
    s += arr[i]
    ans.append(arr[i])
    print_subsets(i+1, arr, ans, s, n, k)
    s -= arr[i]
    ans.pop()
    print_subsets(i+1, arr, ans, s, n, k)
arr = [4, 1, 3, 2, 5]
n = 5
k = 7
print_subsets(0, arr, [], 0, n, k)