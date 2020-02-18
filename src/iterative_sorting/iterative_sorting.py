# TO-DO: Complete the selection_sort() function below 
import time
import random


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
    if arr == []:
        return([])
    count = 0
    new_arr = arr.copy()
    for i in arr:
        if i < 0:
            return("Error, negative numbers not allowed in Count Sort")
        else:
            if i > count:
                count = i
                print(count)
            
    counts = [0 for i in range(count + 1)]
    print(counts)
    for i in arr:
        counts[i] += 1
    #print(counts)
    for i in range(len(counts)):
        if len(counts) - 1 >= i+1:
            counts[i + 1] = counts[i] + counts[i + 1]
        else:
            pass
    counts.insert(0,0)
    counts = counts[:-1]
    for i in arr:
        new_arr[counts[i]] = counts[i]
        counts[i] += 1
    return(new_arr)

a = [random.randint(0,10) for i in range(500)]
b = [random.randint(0,10) for i in range(500)]
c = [random.randint(0,10) for i in range(500)]

start_time = time.time()
selection_sort(a)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
bubble_sort(b)
a.sort()
print("--- %s seconds ---" % (time.time() - start_time))

print(count_sort(c))