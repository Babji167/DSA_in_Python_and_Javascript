def zeros_to_end(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            [arr[i], arr[counter]] = [arr[counter], arr[i]]
            counter+=1
    return arr

arr = [int(i) for i in input("enter elements into the array: ").split()]
result = zeros_to_end(arr)
print(result)
