"""The program to convert the string that the character occurrence to multiply them"""
# input:abcaca
# output:abcaaccaaa

string = input("Enter the string:")
new_string = ""
dictionary = {}
for i in string:
    if i not in dictionary:
        dictionary.setdefault(i, 1)
        new_string += i * dictionary[i]
    else:
        dictionary[i] += 1
        new_string += i * dictionary[i]
print("New String is:",new_string)
