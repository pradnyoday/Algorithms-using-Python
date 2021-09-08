# https://leetcode.com/problems/sort-colors/

nums = [2,0,2,1,1,0]

# Basic Approach: Using sorting algorithm 
# TC: O(nlogn) 
# SC: O(1)

def sortColorsUsingSortingAlgo():
    nums.sort()
    return nums

sortColorsUsingSortingAlgo()
print('sortColorsUsingSortingAlgo:',nums)

# Two Pass Approach: Using counting sort 
# TC: O(n) + O(n) 
# SC: O(1)

nums = [2,0,2,1,1,0]
def sortColorsUsingCountingSortAlgo():
    zeros, ones, twos = 0, 0, 0
    for i in nums:
        if(i == 0): zeros += 1
        elif(i == 1): ones += 1
        else: twos += 1
    for i in range(len(nums)):
        if(i < zeros): nums[i] = 0
        elif(i < zeros + ones): nums[i] = 1
        else: nums[i] = 2
sortColorsUsingCountingSortAlgo()
print('sortColorsUsingCountingSortAlgo:',nums)


# One Pass Approach: Using Dutch Flag Algo 
# TC: O(n) 
# SC: O(1)

nums = [2,0,1]
def sortColorsUsingDutchFlagAlgo():
    n = len(nums)
    low, mid, high = 0, 0, n-1
    while(mid <= high):
        if(nums[mid] == 0):
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif(nums[mid] == 1):
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
sortColorsUsingDutchFlagAlgo()
print('sortColorsUsingDutchFlagAlgo:',nums)