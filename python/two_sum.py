# Given an array of integers:
#   return the indices of the two numbers that add up to the given target

def two_sum(arr, target):
    for i in range(len(arr)):
        temp_target=target-arr[i]
        if (temp_target in arr) and (arr.index(temp_target) != i):
            return [i, arr.index(temp_target)]
