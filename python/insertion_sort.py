# Insertion Sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = i-1

        while prev >= 0 and curr < arr[prev]:
            arr[curr], arr[prev] = arr[prev], arr[curr]
            prev-=1
    return arr
