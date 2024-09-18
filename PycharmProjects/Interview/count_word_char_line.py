# Count number of words,characters,length in file

page = open("waste.txt", mode='r')
number_of_lines = 0
number_of_characters = 0
number_of_words = 0
for lines in page:
    number_of_lines += 1
    line = lines.strip()
    number_of_characters += len(lines)
    list1=lines.split("\n")
    number_of_words+=len(list1)
page.close()
print(f"Number of Characters in page is {number_of_characters}")
print(f"Number of words in page is {number_of_words}")
print(f"Number of lines in page is {number_of_lines}")