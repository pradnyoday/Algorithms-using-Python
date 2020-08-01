def findExpo(num, expo):
    ans = 1
    while(expo):
        if(expo & 1):
            ans *= num
        num *= num
        expo >>= 1
    return ans % 1000000007
    
if __name__ == '__main__':
    num,expo = map(int,input().split())
    print(findExpo(num,expo))
