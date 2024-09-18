def fibonacci(number):
    """Function to print the fibonacci number from range N"""
    first = 0
    second = 1
    # sum1 = 0
    print("Fibonacci series is:", end="")
    while True:
        print(first, end="")
        if second > number:
            break
        first, second = second, first + second
        """sum1 = first + second
        first = second
        second = sum1"""
        print(end=",")
    return


num = int(input("Enter the range:"))
if num <= 0:
    print("Number enter by user is negative.")
else:
    fibonacci(num)
