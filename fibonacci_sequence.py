def fibonacci_sequence(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

n=int(input("Enter the number of terms in the Fibonacci sequence: "))
result=fibonacci_sequence(n)
print(result)
# This code will print the nth Fibonacci number based on user input.
# Note: This implementation is not efficient for large n due to its exponential time complexity.