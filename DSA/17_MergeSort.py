def divide(arr, l, r):
    if(l < r):
        m = (l+r)//2
        divide(arr, l, m)
        divide(arr, m+1, r)
        merge(arr, l, r, m)

def merge(arr, l, r, m):
    s1 = m - l + 1
    s2 = r - m
    leftArr = [0]*s1
    rightArr = [0]*s2

    for i in range(s1):
        leftArr[i] = arr[l+i]
    for j in range(s2):
        rightArr[j] = arr[m+1+j]

    i = j = 0
    k = l

    while(i < s1 and j < s2):
        if(leftArr[i] < rightArr[j]):
            arr[k] = leftArr[i]
            i+=1
        else:
            arr[k] = rightArr[j]
            j+=1
        k+=1

    while(i < s1):
        arr[k] = leftArr[i]
        i+=1
        k+=1

    while(j < s2):
        arr[k] = rightArr[j]
        j+=1
        k+=1

arr = [10,9,8,7,6,5,4,3,2,1]
divide(arr,0,len(arr)-1)
print(arr)