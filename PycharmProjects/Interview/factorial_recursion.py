"""The program is to find the factorial of the number by recursion."""


def factorial(num):
    if num == 0:
        return 1
    return factorial(num - 1) * num


number = int(input("Enter the number:"))
if number < 0:
    print("Factorial of negative number can't be calculated")
else:
    print(f"Factorial of {number} is {factorial(number)}")
