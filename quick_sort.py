# We can impliment using a reccursive function
# assume 0th index as pivot element
# pass 2 array lower and upper 
# lower means value less than pivot
# upper means values > pivot
# return array after complete 

def quickSort(arr):
    if len(arr) < 1:
        return arr
    
    pivot = arr[0]


print(quickSort([3,4,5,2,1,8,43,2]))
