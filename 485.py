def findMaxConsecutiveOnes(nums):
    res = 0 
    count = 0 
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            count = 0 
        res = max(res, count)
    return res

nums = [1,1,0,1,1,1]

print(findMaxConsecutiveOnes(nums))