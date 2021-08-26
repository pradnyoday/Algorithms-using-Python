
def fast_power(num, expo):
    ans = 1
    mod = 1000000007
    while(expo):
        if(expo & 1):
            ans = (ans * num % mod) % mod
        num = num % mod * num % mod
        expo >>= 1
    return ans
    
if __name__ == '__main__':
    num,expo = 3, 5
    print(fast_power(num,expo))