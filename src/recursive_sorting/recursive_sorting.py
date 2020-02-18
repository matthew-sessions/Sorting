# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if arrA == []:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif arrB == []:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrA[0] > arrB[0]:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        else:
            merged_arr[i] = arrA[0]
            arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return(arr)
    arrA, arrB = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
    return merge(arrA, arrB)

print(merge_sort([2,5,6,9,5,56,8,655,11]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
