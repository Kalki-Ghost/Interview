"""program to find all the substring of string"""
string = input("Enter the string:")

list1 = []
for i in range(0, len(string)):
    for j in range(i + 1, len(string) + 1):
        list1.append(string[i:j])

print(f"All the substring of the string '{string}' is {list1}")
