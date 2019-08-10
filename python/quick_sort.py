# Given an array sort the value in ascending order using Quick Sort

def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[-1]
        smaller=[]
        larger=[]
        for i in arr[:-1]:
            if i <= pivot:
                smaller.append(i)
            else:
                larger.append(i)
        return quick_sort(smaller) + [pivot] + quick_sort(larger)
