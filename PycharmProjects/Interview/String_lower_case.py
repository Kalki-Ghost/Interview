"""The program is to convert the uppercase letter to lower case without using the string methods."""

string = input("Enter the string:")
ans = ""
for i in string:
    if 64 < ord(i) < 91:  # i.isupper()
        i = ord(i) + 32

        i = chr(i)
    ans += i
print(ans)
