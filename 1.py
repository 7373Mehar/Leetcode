def twoSum(numbers, target):
    prev_map={}
    for i, n in enumerate(numbers):
        diff = target - n 
        if diff in prev_map:
            return (prev_map[diff],i)
        prev_map[n]=i
    return 


numbers = [2,7,11,13]
target = 9
print(twoSum(numbers, target))

