"""Write a python program that will sum numbers present in given list of data"""
list1 = [1, 2, "a", "b", 4]


def sum_list(list2):
    total = 0
    for i in list2:
        try:
            num = int(i)
        except ValueError:
            print(f"item '{i}' is not a number.")
        else:
            total += num
    return total


print(sum_list(list1))

