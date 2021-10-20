def is_safe(row, col, mat, n):
    i, j = row, col
    while(i >= 0 and j >= 0):
        if(mat[i][j] == 'Q'): return False
        i -= 1
        j -= 1
    i, j = row, col
    while(j >= 0):
        if(mat[i][j] == 'Q'): return False
        j -= 1
    i, j = row, col
    while(i < n and j >= 0):
        if(mat[i][j] == 'Q'): return False
        i += 1
        j -= 1
    return True

def n_queens(col, n, mat):
    if(col == n): 
        for row in mat:
            print(*row)
        return True
    for i in range(n):
        if(is_safe(i, col, mat, n)):
            mat[i][col] = 'Q'
            if(n_queens(col + 1, n, mat)): return True
            mat[i][col] = '-'
    return False
n = 8
mat = [['-' for i in range(n)] for j in range(n)]
n_queens(0, n, mat)