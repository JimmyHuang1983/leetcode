
nums = [2,7,11,-15]
target = -4
res = []
# left, right = 0,1


def two_sum(nums, target):
    for x in range(len(nums)) : 
        right = x +1
        diff = target - nums[x]
        if diff in nums[right:] : 
            res.append(x)
            if diff in nums[right:] : 
                res.append(nums.index(diff, right))
                break
    return res
       
       

answer = two_sum(nums, target)
print(f'Answer is : {answer}')