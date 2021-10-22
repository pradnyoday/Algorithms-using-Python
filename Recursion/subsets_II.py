# Leetcode
# https://leetcode.com/problems/subsets-ii/

def print_subsets(i, ans, arr, n, s):
    if(i == n):
        if(s not in ans):
            ans.append(s.copy())
        return
    s.append(arr[i]) # Pick item
    print_subsets(i+1, ans, arr, n, s)
    s.pop() # Dont Pick item
    print_subsets(i+1, ans, arr, n, s)
    return ans
arr = [4,4,4,1,4]
n = 5
arr.sort()
ans = print_subsets(0, [], arr, len(arr), [])
print(ans)


arr = [1, 2, 2]
n = 3
ans = []
a = print_subsets(0, ans, arr, n, [])
print(a)