#https://www.techiedelight.com/find-pair-with-given-sum-array/

def sum_of_pair(arr, target):
    hash = dict()
    for num in arr:
        if(target - num in hash):
            return (num, target - num)
        else:
            hash[num] = num
    return None        
arr = [8, 7, 2, 5, 3, 1]
target = 10
print(sum_of_pair(arr, target))