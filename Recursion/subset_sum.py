def subset(i, n, arr, ans, s):
    if(i == n):
        ans.append(s)
        return ans
    s += arr[i]
    ans = subset(i+1, n, arr, ans, s)
    s -= arr[i]
    ans = subset(i+1, n, arr, ans, s)
    return ans
arr = [5, 4, 3]
n = 3
ans = subset(0, n, arr, [], 0)
print(ans)