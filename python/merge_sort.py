# Simple Merge Sort Algo
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    res=[]
    mid = int(len(arr) / 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            res.append(right[r])
            r+=1
        else:
            res.append(left[l])
            l+=1

    res += left[l:]
    res += right[r:]
    return res
