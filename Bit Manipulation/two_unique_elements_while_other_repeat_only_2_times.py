arr = [5, 4, 1, 4, 6, 5, 1, 2]
ans = 0
for i in arr:
    ans ^= i
ans &= -(ans - 1)
a, b = 0, 0
for i in arr:
    if(ans & i):a ^= i
    else:b ^= i
print(a, b)