def binary_search(arr, target, offset=0):
    if len(arr) > 0:
        mid = len(arr) // 2
        if arr[mid] == target:
            print(f"Element {target} found at index {mid + offset}")
            return mid + offset
        elif target < arr[mid]:
            return binary_search(arr[:mid], target, offset)
        else:
            return binary_search(arr[mid + 1:], target, offset + mid + 1)

    print(f"Element {target} not found")
    return -1



arr2=[int(i) for i in input("Enter the elements to the array: ").split()]
target2=int(input("Enter the second target element to search: "))
binary_search(sorted(arr2), target2)

# time complexity: O(log n) for both worst and average case
# best case: O(1) when the middle element is the key        
# space complexity: O(log n) due to recursive stack space
# best case occurs when the key is found at the middle index
