"""The program is to print the values of the list without using the loop and slicing"""

def without_loop(list1, start, end):
    if 0 < start <= end and len(list1) > start:
        print(list1[start])
        return without_loop(list1, start + 1, end)


# def without_loop(list1, start, end):
#     if start >= end or start < 0 or len(list1) <= start:
#
#         return
#     else:
#         print(list1[start])
#         return without_loop(list1, start + 1, end)


list2 = list(map(int, input("Enter the list:").split()))
start1 = int(input("Enter the Starting index:"))
end1 = int(input("Enter the ending index:"))
without_loop(list2, start1, end1)
