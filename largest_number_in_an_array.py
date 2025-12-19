def largest_number_in_array(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if (arr[i]>max):
            max = arr[i]
    return max

arr = [int(i) for i in input("enter number into the array: ").split()]
result = largest_number_in_array(arr)
print("the largest number is: "+str(result))        