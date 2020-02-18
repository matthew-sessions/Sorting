import random

def partition(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else: #Handling > or =
            right.append(item)
    #print(left, pivot, right)
    return left, pivot, right

def quicksort(data):
    if data == []:
        #print('done')
        return data
    
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)

# def quicksort(arr):
#     if arr:
#         pivot = random.choice(arr)
#         low = [n for n in arr if n < pivot]
#         middle = [n for n in arr if n == pivot]
#         high = [n for n in arr if n > pivot]
#         return [*quicksort(low), *middle, *quicksort(high)]
#     else:
#         return []


li = [random.randint(1, 5999955) for i in range(10)]
print(4)
print(quicksort(li))