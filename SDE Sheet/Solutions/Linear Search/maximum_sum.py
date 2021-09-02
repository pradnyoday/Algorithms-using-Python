#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/
def maximum_sum(n, arr):
    ans, l = 0, 0
    for i in arr:
        if(i >= 0):
            l += 1
            ans += i
    return (ans, l)
n = 5
arr = [1, 2, -4, -2, 3]
print(maximum_sum(n, arr))