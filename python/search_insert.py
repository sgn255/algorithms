# Given a sorted array and a target value:
# return the index if the target is found
# else: return the index where it would be if it were inserted in order.

def search_insert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
