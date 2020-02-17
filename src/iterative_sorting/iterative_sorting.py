# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    lenth = len(arr)
    for i in range(0, lenth - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, lenth):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        print(arr[smallest_index], arr[cur_index])
        cur = arr[i]
        smallest = arr[smallest_index]
        arr[i] = smallest
        arr[smallest_index] = cur


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    lenth  = len(arr)
    for i in range(0, lenth):
        base_index = i
        for j in range(0, lenth - base_index):
            front = j + 1
            if front < lenth - base_index:
                if arr[j] > arr[front]:
                    arr_min = arr[j+1]
                    arr_max = arr[j]
                    arr[j] = arr_min
                    arr[j+1] = arr_max

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

a = [3,6,2,5,8,9,4,6,85]
print(bubble_sort(a))
print(a)