def second_largest_number(arr):
    if len(arr) < 2:
        return "Array must contain at least two elements."

    first_max = float('-inf')
    second_max = float('-inf')

    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif second_max < num < first_max:
            second_max = num

    if second_max == float('-inf'):
        return "No second largest number found (all elements are equal)."

    return second_max

arr = [int(i) for i in input("enter numbers into the array: ").split()]
result = second_largest_number(arr)
print(result)