def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr=[int(i) for i in input("enter the elements into the array: ").split()]
result = bubble_sort(arr)
print(result)
