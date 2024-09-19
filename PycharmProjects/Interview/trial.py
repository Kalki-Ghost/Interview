"""The program to print the list without using loop(Recursion)"""


def without_loop(list1, start, end):
    if start >= end or start < 0 or len(list1) >= start:
        return
    else:
        print(list1[start])
        return without_loop(list1, start + 1, end)


list2 = eval(input("Enter the list:"))
start1 = int(input("Enter the Starting index:"))
end1 = int(input("Enter the ending index:"))
without_loop(list2, start1, end1)
