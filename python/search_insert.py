# Given a sorted array and a target value:
# return the index if the target is found
# else: return the index where it would be if it were inserted in order.

def search_insert(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        arr.append(target)
        arr.sort()
        return arr.index(target)
