'''
Project 02 - Library System
Ye Bo Gong
10/25/23
This program simulates a library system allowed the user to add a book, borrow a book, return a book, list all books, or exit the program.
'''

#Function to display the main menu and all the choices.
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')

#Function to verify if the ISBN is a valid ISBN
def valid_ISBN(isbn):
    factors = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    if len(isbn) == 13 and isbn.isdigit():
        total = sum([int(isbn[i]) * factors[i] for i in range(13)])
        return total % 10 == 0
    else:
        return False

#function to add a book to the list
def addBook(allBooks):
    #Input book name
    bookName = input("Book name> ")
    while '*' in bookName or '%' in bookName: #checking if * or % is in the user input
        print("Invalid Book name!")
        bookName = input("Book name> ")

    authorName = input("Author name> ")
    #Make sure edition is correct
    while True:
        try:
            edition = int(float(input("Edition> ")))
            break
        except ValueError:
            pass
    #Make sure the ISBN is valid and see if there are any duplicate ISBNs
    while True:
        isbn = input("ISBN> ")
        if len(isbn) != 13 or not isbn.isdigit():
            print("Invalid ISBN.")
        elif valid_ISBN(isbn):
            if isbn not in [book[0] for book in allBooks]:
                break
            else:
                print("Duplicate ISBN is found! Cannot add the book.")
                return
        else:
            print("Invalid ISBN")
            return
    #Append new book to the library
    allBooks.append([isbn, bookName, authorName, edition, []])
    print("A new book is added successfully.")

#function to borrow books
def borrowBooks(allBooks, borrowedISBNs):
    borrower = input("Borrower name> ")
    searchTerm = input("Search term> ")

    matchedBooks = []
    #Searching for books based on terms
    for book in allBooks:
        if book[0] not in borrowedISBNs:
            if searchTerm[-1] == "*":
                if searchTerm[:-1].lower() in book[1].lower():
                    matchedBooks.append(book)
            elif searchTerm[-1] == "%":
                if book[1].lower().startswith(searchTerm[:-1].lower()):
                    matchedBooks.append(book)
            else:
                if searchTerm.lower() == book[1].lower():
                    matchedBooks.append(book)

    if not matchedBooks:
        print("No books found!")
        return
    #Making books borrowed
    for book in matchedBooks:
        if book[0] not in borrowedISBNs:
            book[4].append(borrower)
            borrowedISBNs.append(book[0])
            print(f'-"{book[1]}" is borrowed!')
        else:
            print("No books found!")

#function to return a book
def returnBook(allBooks, borrowedISBNs):
    isbn = input("ISBN to return> ")
    for index, book in enumerate(allBooks):
        if book[0] == isbn:
            if isbn in borrowedISBNs:
                borrowedISBNs.remove(isbn)
                print(f'"{book[1]}" is returned.')
                return
    print("No book is found in the borrowed books list!")

#function to list all books
def listBooks(allBooks, borrowedISBNs):
    for book in allBooks:
        availability = "[Available]" if book[0] not in borrowedISBNs else "[Unavailable]"
        print("---------------")
        print(availability)
        print(f"{book[1]} - {book[2]}")
        print(f"E: {book[3]} ISBN: {book[0]}")
        print(f"Borrowed by: {book[4]}")

#main function to start the program
def start():
    #Starting collection of books
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    #starting collection of borrowed books
    borrowedISBNs = []
    #checking userInput
    while True:
        printMenu()
        choice = input("Your selection> ").lower()

        if choice in ['1', 'a']:
            addBook(allBooks)
        elif choice in ['2', 'r']:
            borrowBooks(allBooks,borrowedISBNs)
        elif choice in ['3', 't']:
            returnBook(allBooks,borrowedISBNs)
        elif choice in ['4', 'l']:
            listBooks(allBooks,borrowedISBNs)
        elif choice in ['5', 'x']:
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            listBooks(allBooks,borrowedISBNs)
            exit()
        else:
            print("Wrong selection! Please select a valid option.")

#invoke the start function
start()
