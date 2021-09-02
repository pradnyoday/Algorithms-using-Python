n, m = 3, 4
def findWays(n, m):
    if(n == 1 or m == 1):
        return 1
    return findWays(n, m-1) + findWays(n-1, m)
print(findWays(n, m))