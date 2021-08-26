def gcd(a, b):
    if(b == 0):return a
    return gcd(b, a % b)
if(__name__ == "__main__"):
    gcd = gcd(24, 60)
    print(gcd)