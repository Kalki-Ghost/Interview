"""Maximum product of two number in a list"""

list1 = list(map(int, input("Enter the list:").split()))


def maximum(list2):
    a = list1[0]
    b = list1[1]
    for i in range(0, len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if list1[i] * list1[j] > a * b:
                a = list1[i]
                b = list1[j]
    return a, b


print(f"Maximum product numbers of the list is {maximum(list1)}")
