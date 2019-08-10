# Selection Sort

def selection_sort(arr):
    for i in range(1,len(arr)):
        s_idx = arr[i:].index(min(arr[i:]))+i
        if arr[s_idx] < arr[i-1]:
            arr[i-1], arr[s_idx] = arr[s_idx], arr[i-1]
    return arr
