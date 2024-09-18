"""Write the python program for printing armstrong numbers between 1 and 1000"""
import math

start = int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
for i in range(start,end+1):
    length = len(str(i))
    number = i
    sum1 = 0
    while number != 0:
        mod = number % 10
        sum1 += math.pow(mod, length)
        number //= 10
    if i == sum1:
        print(i,end=',')

