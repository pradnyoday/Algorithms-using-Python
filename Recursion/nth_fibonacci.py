n = 12
def fibonacci(n):
    if(n <= 1): return n
    return fibonacci(n - 1) + fibonacci(n - 2)
ans = fibonacci(n)
print(ans)