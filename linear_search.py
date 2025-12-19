def linear_search(key, Myarray):
    for i in range(len(Myarray)):
        if Myarray[i] == key:
            print("Element found at index:", i)
            return True
    print("Element not found")
    return False


key=int(input("Enter the key to search: "))
Myarray=[int(i) for i in input("Enter the elements of the array separated by space: ").split()]
linear_search(key, Myarray)

# time complexity: O(n) both worst and average case
# best case: O(1) when the first element is the key
# best case occurs when the key is found at the first index
# space complexity: O(1)