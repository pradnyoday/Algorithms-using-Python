# print all subsets whose sum is equal to k with repetition of elements allowed
def all_subsets_whose_sum_is_equal_to_k_with_repetition_of_elements_allowed(i, arr, ans, s, n, k):
    if(s == k):
        print(ans)
        return
    if(i == n or s > k): 
        return
    
    if(s + arr[i] <= k):
        ans.append(arr[i])
        s += arr[i]
        all_subsets_whose_sum_is_equal_to_k_with_repetition_of_elements_allowed(i, arr, ans, s, n, k)
        s -= arr[i]
        ans.pop()
    all_subsets_whose_sum_is_equal_to_k_with_repetition_of_elements_allowed(i+1, arr, ans, s, n, k)

arr = [1, 2, 3]
n = 3
k = 4
all_subsets_whose_sum_is_equal_to_k_with_repetition_of_elements_allowed(0, arr, [], 0, n, k)