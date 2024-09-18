# It is menu-driven program.It gives option to user for work

while True:
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        print(f"Addition is:{n1 + n2}")
    elif choice == 2:
        print(f"Subtraction is:{n1 - n2}")
    elif choice == 3:
        print(f"Multiplication is:{n1 * n2}")
    elif choice == 4:
        print(f"division is:{n1 / n2}")
    else:
        print("Invalid choice.")
    flag = input("Do you want to continue?(y/n)")
    if flag.upper() == 'N':
        break
