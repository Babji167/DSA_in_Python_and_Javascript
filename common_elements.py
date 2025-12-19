def common_elements(arr1,arr2):
    common=[]
    for i in arr1:
        for j in arr2:
            if i==j:
                common.append(i)
    return common

arr1=[int(i) for i in input("Enter the elements of the first array: ").split()]
arr2=[int(i) for i in input("Enter the elements of the second array: ").split()]
result = common_elements(arr1, arr2)        
print("Common elements:", result)

# Time complexity: O(n*m) where n is the length of arr1 and m is the length of arr2
# Space complexity: O(k) where k is the number of common elements found 
# Best case: O(1) when there are no common elements
# Worst case: O(n*m) when all elements of arr1 are present in arr2
# Average case: O(n*m) as it depends on the distribution of elements in both arrays