"""Program to find the reverse of the string"""
# input:sky is blue
# output:blue is sky

# string = input("Enter the string:").split()
# print(" ".join(string[::-1]))

"""Program to find the unique elements in the list"""
# input:[1,2,2,3,3,4,5,5,5,6,6]
# output:[1,4]

# list1 = list(map(int, input("Enter the list(enter element by space):").split()))
# unique = []
# for i in list1:
#     if list1.count(i) == 1:
#         unique.append(i)
# print(unique)

# for i in range(0, len(list1)):
#     flag = 1
#     for j in range(0, len(list1)):
#         if i == j:
#             continue
#         elif list1[i] == list1[j]:
#             flag = 0
#             break
#     if flag:
#         unique.append(list1[i])
# print(unique)


"""Program to find the number of same characters in string"""
# input:"a,a,a,b,b,c,c,c"
# output:-a:3,b:3,c:3
string=input("Enter the string:")
visited=[]
for i in string:
    if i not in visited and i!=",":
        print(f"{i}:{string.count(i)}",end=",")
        visited.append(i)
