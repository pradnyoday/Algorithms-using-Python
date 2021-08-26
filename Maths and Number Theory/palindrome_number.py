n = 404
n1 = n
newno = 0
while(n1):
    ld = n1%10
    newno = newno*10 + ld
    n1 //= 10
if(n == newno):print('Yes')
else:print('No')
