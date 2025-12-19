def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr=[int(i) for i in input("enter the numbers into the array: ").split()]
result=insertion_sort(arr)
print(result)
