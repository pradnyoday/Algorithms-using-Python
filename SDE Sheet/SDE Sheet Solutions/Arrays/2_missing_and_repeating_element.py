# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/




# Sorting Approach: Using sorting algorithm 
# TC: O(nlogn) 
# SC: O(1)

nums = [4, 3, 6, 2, 1, 1]
def missing_and_repeating_num_using_sorting():
    nums.sort()
    n = len(nums)
    missing, repeating = float("inf"), float("inf")
    for i in range(len(nums)-1):
        if(nums[i] == nums[i+1]): repeating = nums[i+1]
        if(nums[i]+1 != nums[i+1]): missing = i+1
    return [missing, repeating]
missing, repeating = missing_and_repeating_num_using_sorting()[0], missing_and_repeating_num_using_sorting()[1]
print('missing_and_repeating_num_using_sorting:')
print('missing: {0}\nrepeating: {1}\n'.format(missing, repeating))


# Count Array elements method
# TC: O(n) + O(n)
# SC: O(n)

nums = [4, 3, 6, 2, 1, 1]
def missing_and_repeating_num_using_count_array():
    n = len(nums)
    count = [0]*(n+1)
    missing, repeating = float("inf"), float("inf")
    for i in nums:
        if(count[i] == 1): 
            repeating = i
        count[i] = 1
    for i in range(1, len(count)):
        if(count[i] == 0):
            missing = i
    return [missing, repeating]
missing, repeating = missing_and_repeating_num_using_count_array()[0], missing_and_repeating_num_using_count_array()[1]
print('missing_and_repeating_num_using_count_array:')
print('missing: {0}\nrepeating: {1}\n'.format(missing, repeating))

