def print_paths(i, j, n, m, d1, d2, ans):
    if(i >= n or j >= m): return
    if(i == d1 and j == d2): 
        print(ans)
        return
    ans.append('D')
    print_paths(i + 1, j, n, m, d1, d2, ans)
    ans.pop()
    ans.append('R')
    print_paths(i , j + 1, n, m, d1, d2, ans)
    ans.pop()
n = 4
m = 2
print_paths(0, 0, n, m, 2, 1, [])