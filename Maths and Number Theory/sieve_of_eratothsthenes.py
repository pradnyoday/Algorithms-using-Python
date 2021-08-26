def sieve_of_eratosthenes(n):
    isPrime = [True for i in range(n+1)]
    isPrime[0] = False
    isPrime[1] = False
    i = 2
    while(n >= i*i):
        for j in range(2*i, n+1, i):
            isPrime[j] = False
        i += 1
    return isPrime

if __name__ == "__main__":
    n = 13
    arr = sieve_of_eratosthenes(n)
    print(arr[n])