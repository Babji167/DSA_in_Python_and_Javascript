def fibonacci(n,lookup):
    if lookup[n] is not None:
        return lookup[n]
    if n==0 or n==1:
        lookup[n]=1 
    else:
        lookup[n] = fibonacci(n-1,lookup) + fibonacci(n-2,lookup)   
    return lookup[n]

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    lookup = [None] * (n + 1)
    result = fibonacci(n, lookup)
    print(f"The {n}th Fibonacci number is: {result}")

# time complexity: O(n)