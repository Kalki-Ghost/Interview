"""The program to import the employee detail file and extract the information made another file employee bonus and the 2000 as a bonus if employee salary is greater than 35000"""

f1 = open("employee_detail.txt", mode='r')
f2 = open("Bonus_file.txt", mode='w')
lines = list(f1.readlines())
list1 = [lines[0]]

for i in range(1, len(lines)):
    line = lines[i].split('|')
    salary = int(line[2])
    if salary >= 35000:
        bonus = 2000
        list1.append(f"{line[0]}|{line[1]}|{salary + bonus}\n")
    else:
        list1.append(f"{line[0]}|{line[1]}|{salary}\n")

f2.writelines("".join(list1))
f1.close()
f2.close()
