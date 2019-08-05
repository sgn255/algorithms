# Given an array of integers:
#   return the indices of the two numbers that add up to the given target

def two_sum(nums, target):
    for i in range(len(nums)):
        temp_target=target-nums[i]
        if (temp_target in nums) and (nums.index(temp_target) != i):
            return [i, nums.index(temp_target)]
