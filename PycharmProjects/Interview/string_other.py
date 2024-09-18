"""The program to convert the string into short form"""
# input:aaaabbbccd
# output:4a3b2c1d
string = input("Enter the string:")
new_string = ""
temp = string[0]
temp1 = string[1]
num = 1
for i in range(1, len(string)):
    temp1 = string[i]
    if temp == temp1:
        num += 1
    else:

        new_string += str(num) + temp
        num = 1
        temp = temp1

new_string += str(num) + temp
print(new_string)
