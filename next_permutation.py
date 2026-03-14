def nextPermutation(arr):
    n = len(arr)
    pivot = -1
    
    # Step 1: Find pivot
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break
    
    # Step 2: If no pivot, reverse whole array
    if pivot == -1:
        arr.reverse()
        return arr  # <-- return result
    
    # Step 3: Find smallest bigger element to swap
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break
    
    # Step 4: Reverse tail
    arr[pivot + 1:] = reversed(arr[pivot + 1:])
    
    return arr  # <-- return result

# Example usage
print(nextPermutation([1,3,4,6,2,7,9,8,5]))  