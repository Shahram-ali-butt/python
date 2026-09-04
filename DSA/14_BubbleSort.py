'''Uncomment the comments to make the algorithm adaptive'''
def bubble_sort(arr):
    n = len(arr)
    # swaped = False
    for i in range(n):
        print("Number of iteration: ",i)
        for j in range(n - 1 - i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # swaped = True
        # if not swaped: break
        # swaped = False 
    return arr

print(bubble_sort([1,9,8,7,6,5,4,3,2,10]))