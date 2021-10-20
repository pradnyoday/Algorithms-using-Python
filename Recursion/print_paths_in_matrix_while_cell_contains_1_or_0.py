# print_paths_in_matrix_while_cell_contains_1_or_0.
# We can move only if cell contains 1
def print_paths(i, j, n, m, mat, ans):
    if(i >= n or j >= m or mat[i][j] == 0): return
    if(i == n-1 and j == m-1):
        print(ans)
        return
    ans.append('D')
    print_paths(i+1, j, n, m, mat, ans)
    ans.pop()
    ans.append('R')
    print_paths(i, j+1, n, m, mat, ans)
    ans.pop()
n = 3
m = 3
mat = [[1, 0, 1], [1, 1, 0], [1, 1, 1]]
visited = [[0 for i in range(m)] for i in range(n)]
print_paths(0, 0, n, m, mat, [])