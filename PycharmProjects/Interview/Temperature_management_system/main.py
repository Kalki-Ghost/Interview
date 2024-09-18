"""Program to import the file of temperatures and show the menu-driven purpose"""


def day_wish_temp():
    """This function print day wise temperatures"""
    print("Days wise temperature:")
    for d in temp_day:
        print(f"{d.title()}:{temp_day[d]}")


def average():
    sum1 = 0
    for i in temp_day:
        sum1 += temp_day[i]
    return sum1 / len(temp_day)


def minimum():
    """This function return the minimum temperature"""
    min1 = temp_day["MONDAY"]
    day = "MONDAY"
    for i in temp_day:
        if temp_day[i] <= min1:
            day = i
            min1 = temp_day[i]
    return min1, day


def maximum():
    """This function return the maximum temperature"""
    max1 = temp_day["MONDAY"]
    day = "MONDAY"
    for i in temp_day:
        if temp_day[i] >= max1:
            day = i
            max1 = temp_day[i]
    return max1, day


def below_zero():
    """Print the below zero temperature days"""
    day = []
    for i in temp_day:
        if temp_day[i] <= 0:
            day.append(i)
    print("Days below zeo temperature:")
    for j in day:
        print(f"{j.title()}:{temp_day[j]}")


def separator():
    """print the days above and below the temperature by separator"""
    num = float(input("Enter the separator temperature:"))
    below = []
    above = []
    for i in temp_day:
        if num <= temp_day[i]:
            above.append(i)
        else:
            below.append(i)

    print("Temperature above the separator:")
    for j in above:
        print(f"{j.title()}:{temp_day[j]}")

    print("Temperature below the separator:")
    for j in below:
        print(f"{j.title()}:{temp_day[j]}")


f = open("temperatures_list.txt", mode='r')
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
line_num = 0
temp = []
temp_day = {}
for line in f:
    line = line.strip('\n')
    temp.append(float(line))
    temp_day[days[line_num]] = float(line)
    line_num += 1
print(temp_day)
f.close()

while True:
    print("Select from the following:")
    print("""1.Show day wise temperatures
2.Show average of all temperature
3.Show minimum temperature
4.Show maximum temperature.
5.Show days having below zero temperature
6.Show days using seperator""")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        day_wish_temp()

    elif choice == 2:
        print(f"Average of all temperature is {round(average(), 2)}")

    elif choice == 3:
        ans = minimum()
        print(f"Minimum temperature is {ans[0]} on {ans[1].title()}")
    elif choice == 4:
        ans = maximum()
        print(f"Maximum temperature is {ans[0]} on {ans[1].title()}")
    elif choice == 5:
        below_zero()
    elif choice == 6:
        separator()
    else:
        print("You enter the wrong choice.")

    flag = input("Do you want to continue?(y/n)")
    if flag.upper() != "Y":
        break
