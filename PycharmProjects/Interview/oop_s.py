"""The program is display the working with class and object."""


class Movie:
    def __init__(self, title, cost, pages):
        self.pages = pages
        self.title = title
        self.cost = cost

    def info(self):
        print(f"Title of the book is \"{self.title}\"")
        print(f"Cost of the book is {self.cost}")
        print(f"No of pages in the book is {self.pages}")
        print()


list1 = []
while True:
    title1 = input("Enter the title of the book:")
    cost1 = int(input("Enter the cost of the book is:"))
    page = int(input("Enter the no of pages in book:"))

    obj = Movie(title1, cost1, page)
    list1.append(obj)
    print("Book added to list successfully.")
    flag = input("Do you want add another book?(y/n)")
    if flag.upper() != "Y":
        break

for i in list1:
    i.info()
