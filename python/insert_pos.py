## Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
