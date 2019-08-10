## Given an array nums and a value val, remove all instances of that value in-place.

def removeElement(nums, val):
    while val in nums :
        del nums[nums.index(val)]
    return (nums)
