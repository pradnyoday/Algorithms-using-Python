d = ['D', 'R', 'U', 'L']
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def print_paths(i, j, n, m, d1, d2, ans, visited):
    if(i >= n or j >= m or i < 0 or j < 0 or visited[i][j] == 1): return
    if(i == d1 and j == d2): 
        print(ans)
        return
    visited[i][j] = 1
    for x in range(4):
        ans.append(d[x])
        print_paths(i+di[x], j+dj[x], n, m, d1, d2, ans, visited)
        ans.pop()
    visited[i][j] = 0
n = 4
m = 2
visited = [[0 for i in range(m)] for i in range(n)]
print_paths(0, 0, n, m, 2, 1, [], visited)