"""The program is to form the string by given character and numbers."""
"""input: A3B1C2
output:AAABCC"""

string = input("Enter the string:")
output = ""
ch = ""
for char in string:
    if char.isalpha():
        ch = char
    else:
        digit = int(char)
        output += ch * digit
print(output)
