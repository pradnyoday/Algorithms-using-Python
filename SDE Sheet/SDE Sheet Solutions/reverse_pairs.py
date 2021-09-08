# https://leetcode.com/problems/reverse-pairs/

# Brute force approach 
# TC: O(n^2) --> Time Limit Exceeded
# SC: O(1)

def reversePairsUsingBruteForce(nums):
    ans = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(2 * nums[j] < nums[i]): ans += 1
    return ans
nums = [2,4,3,5,1]
print(reversePairsUsingBruteForce(nums))

# 