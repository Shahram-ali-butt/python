def insertion_sort(arr):
    n = len(arr)
    if n < 2: return arr
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key
    return arr

print(insertion_sort([10,9,8,7,6,5,4,3,2,1]))