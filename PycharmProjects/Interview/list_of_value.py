# program to print number of list of values in dictionary55454re
dictionary = {"Arun": ["Puc", 21], "Venkatesh": ["Engineering", 30], "ram": 30}
count = 0
for item in dictionary:
    if isinstance(dictionary[item], list):
        count += 1
print(f"Number of list of items in dictionary:{count}")
