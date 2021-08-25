arr = [2, 2, 2, 10, 2]
k = 3
bin = [0 for i in range(32)]
for i in range(32):
    for j in arr:
        if(j & (1 << i)):
            bin[i] += 1
res = 0
bin.reverse()
for i in range(32):
    if(bin[i] % k):bin[i] = 1
    else:bin[i] = 0
ans = 0
for i in bin:
    ans = (ans << 1) | i
print(ans)