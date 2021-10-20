def isPalindrome(s, l, r):
    if(l >= r): return True
    if(s[l] != s[r]): return False
    return isPalindrome(s, l + 1, r - 1)
s = "pradnyoday"
n = 10
s1 = "tenet"
n1 = 5
print(isPalindrome(s, 0, n-1))
print(isPalindrome(s1, 0, n1-1))