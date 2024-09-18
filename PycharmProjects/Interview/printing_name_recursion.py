def printer(name, number):
    if number == 0:
        return
    print(f"{number}:{name}")
    return printer(name, number - 1)


name1 = input("Enter the name:")
number1 = int(input("Enter the number of times to print:"))
if number1 <= 0:
    print("Enter the positive number.")
else:
    printer(name1, number1)
