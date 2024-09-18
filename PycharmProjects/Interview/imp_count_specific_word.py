"""Write the python program to display the words that are repeated more than or equal to N times in tha text"""

string = input("Enter the string:")
number = int(input("Enter the number:"))
list1 = string.split()
ans = dict()
for item in list1:
    count = list1.count(item)
    if count >= number and item not in ans:
        ans[item]=count
if ans:
    print(ans)
else:
    print("NA")

