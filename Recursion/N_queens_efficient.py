def is_safe(row, col, mat, n, rowHash, upperDiagHash, lowerDiagHash):
    if(rowHash[row] == 1 or upperDiagHash[n-1+ row - col] == 1 or lowerDiagHash[row + col] == 1): return False
    return True

def n_queens(col, n, mat, rowHash, upperDiagHash, lowerDiagHash):
    if(col == n): 
        for row in mat:
            print(*row)
        return True

    for i in range(n):
        if(is_safe(i, col, mat, n, rowHash, upperDiagHash, lowerDiagHash)):
            mat[i][col] = 'Q'
            rowHash[i] = 1
            lowerDiagHash[i+col] = 1
            upperDiagHash[n-1 + i - col] = 1
            if(n_queens(col + 1, n, mat, rowHash, upperDiagHash, lowerDiagHash)): return True
            mat[i][col] = '-'
            rowHash[i] = 0
            lowerDiagHash[i+col] = 0
            upperDiagHash[n-1 + i - col] = 0
    return False

n = 8
mat = [['-' for i in range(n)] for j in range(n)]
rowHash = [0] * n
upperDiagHash = [0] * (n-1) * 2
lowerDiagHash = [0] * (n-1) * 2
n_queens(0, n, mat, rowHash, upperDiagHash, lowerDiagHash)