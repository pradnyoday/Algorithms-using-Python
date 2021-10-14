def print_subsets(i, ans, arr, n):
    if(i == n):
        print(ans)
        return
    ans.append(arr[i]) # Pick item
    print_subsets(i+1, ans, arr, n)
    ans.pop() # Dont Pick item
    print_subsets(i+1, ans, arr, n)
arr = [1, 2, 3]
n = 3
print_subsets(0, [], arr, n)