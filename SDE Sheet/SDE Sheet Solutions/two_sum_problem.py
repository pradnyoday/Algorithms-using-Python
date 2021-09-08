# https://leetcode.com/problems/two-sum/

# two Sum With Brute Force Approach -> 
# TC: O(n^2) 
# SC: o(n)
def twoSumWithBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]
    return None

nums = [2,7,11,15]
target = 9
print('twoSumWithBruteForce:',twoSumWithBruteForce(nums, target))

# two Sum using dictionary Approach -> 
# TC: O(n) 
# SC: O(n)

def twoSumUsingDict(nums, target):
    d = dict()
    for i in range(len(nums)):
        if(target - nums[i] in d):
            return [d[target - nums[i]], i]
        d[nums[i]] = i
    return None
nums = [2,7,11,15]
target = 9
print('twoSumUsingDict:',twoSumUsingDict(nums, target))