# lets try 2 pointer approch 
# take left and right from given array
# check for 

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # print(i)
        for index in range(n - i -1):
            # print(n - i -1)
            left, right = index, index + 1
            if arr[left] > arr[right]:
                arr[right], arr[left] = arr[left], arr[right]

    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quicksort(lesser) + [pivot] + quicksort(greater)

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)

# print(bubbleSort([3,33,1,2,4,7,12,1]))