def rotate_left(arr, d):
    n = len(arr)
    if n == 0 or d % n == 0:
        return arr  # No rotation needed

    d %= n  # Normalize d if d > n

    def reverse(sub_arr, start, end):
        while start < end:
            sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)

    # Step 2: Reverse remaining n-d elements
    reverse(arr, d, n - 1)

    # Step 3: Reverse the whole array
    reverse(arr, 0, n - 1)

    return arr

arr=[int(i) for i in input("enter the elements into sequence: ").split()]
d=int(input("enter number of rotations: "))
result = rotate_left(arr, d)
print(result)