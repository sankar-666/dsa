# we need to find a item form a sorted array with binry search
# time complexity will be O(log n)
# we can do this with a 2 pointer approch
# take left, right and find the middle element in a loop
# check if middle == target return middle
# else check middle > target right - 1 else left + 1

def binarySearch(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2 

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

def linearSearch(arr, target):
    
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9], 8))
print(linearSearch([1,2,3,4,5,6,7,8,9], 8))
