def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i, n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selection_sort([10,9,8,7,6,5,4,3,2,1]))