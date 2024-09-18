"""Program to make the operation on integer and raise exception if any exception in input"""


class OperatorError(Exception):
    pass


class OperationError(Exception):
    pass


def calculator():
    operator = ('+', '-', '*', '/')

    try:
        input_ope = input("Enter the input:")
        input_ope = input_ope.split()
        ope = input_ope[1]
        if len(input_ope) != 3:
            raise OperationError("Please enter two operands and operator in between separated by spaces.")
        if ope not in operator:
            raise OperatorError(f"{ope} is not valid,please enter an operator from {operator}.")
        num1 = float(input_ope[0])
        num2 = float(input_ope[2])
        if ope == '/' and num2 == 0:
            raise ZeroDivisionError("Can't divide by zero.")
    except Exception as e:
        print(e)
        print("Try again.")
        calculator()
    else:
        if ope == '+':
            result = num1 + num2
        elif ope == '-':
            result = num1 - num2
        elif ope == '*':
            result = num1 * num2
        elif ope == '/':
            result = num1 / num2
    finally:
        return f"{num1}{ope}{num2}={result}"


final_result = calculator()
print(final_result)
