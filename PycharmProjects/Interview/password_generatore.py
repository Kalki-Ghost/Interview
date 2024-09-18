"""The program to generate the random password."""

import random
import string

number=int(input("Enter the number of characters in password:"))
list1 = string.ascii_letters + string.ascii_uppercase + string.digits + string.punctuation
password = random.sample(list1, number)

password = "".join(password)
print(password)
