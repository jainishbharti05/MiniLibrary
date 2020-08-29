class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our Library , {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
        else:
            print(f"{book} is now issued to {self.lendDict[book]}")

    def returnBook(self, book):
        self.lendDict.pop(book)

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")


if __name__ == '__main__':
    BCREC = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'],
                    "BCREC Library")

    while True:
        print(f"Welcome to the {BCREC.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = int(input())

        if user_choice not in [1, 2, 3, 4]:
            print("Please enter a valid option")
            continue

        if user_choice == 1:
            BCREC.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            BCREC.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            BCREC.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            BCREC.returnBook(book)

        print("Press q to quit and c to continue: ")
        user_choice2 = input()
        if user_choice2 == 'q':
            exit()
        elif user_choice2 == 'c':
            continue



