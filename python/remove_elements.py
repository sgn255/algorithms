# Given an array and a value:
#   remove all instances of that value in-place

def remove_element(arr, val):
    while val in arr :
        del arr[arr.index(val)]
    return arr
