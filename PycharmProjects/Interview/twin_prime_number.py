"""The program is to find the twin prime number."""
"""Rules:difference between the two number is two and they are both must be prime number."""


def prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
if prime(number1) and prime(number2):
    if abs(number2 - number1) == 2:
        print(f"{number1} and {number2} are twin prime number.")
    else:
        print(f"{number1} and {number2} are not twin prime number.")
else:
    print(f"{number1} and {number2} are not twin prime number.")

# number = list(map(int, input("Enter the two number:").split()))
# if abs(number[1] - number[0]) == 2:
#     flag = 1
#     for i in number:
#         for num in range(2, i):
#             if i % num == 0:
#                 print("They are not twin prime numbers.")
#                 flag = 0
#                 break
#         if flag == 0:
#             break
#     if flag:
#         print("They are twin prime numbers.")
# else:
#     print("They are not twin prime numbers.")
