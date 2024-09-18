"""The program to switch the cases of the string and first letter most be uppercase"""
# input:VEnKatEsH
# output:VeNkATeSh
string = input("Enter the string:")
new_string = ""
if 65 <= ord(string[0]) <= 90:
    new_string += string[0]
else:
    new_string += chr(ord(string[0]) - 32)

for i in string[1:]:
    """The loop for swap the case of alphabet"""
    # new_string += i.swapcase()
    if 65 <= ord(i) <= 90:
        new_string += chr(ord(i) + 32)
    else:
        new_string += chr(ord(i) - 32)

print("The new string is:", new_string)
