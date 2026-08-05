class Library:
    def __init__(self):
        self.books = {}      # Book Number -> Book Details
        self.patrons = {}    # Patron Number -> Patron Details
        self.borrowed = {}   # Patron Number -> Borrowed Books

        # Enter Books
        total_books = int(input("Enter the number of books: "))

        for i in range(total_books):
            print(f"\nEnter details for Book {i + 1}")
            book_no = input("Book Number: ")
            book_name = input("Book Name: ")

            self.books[book_no] = {
                "name": book_name,
                "quantity": 1
            }

        # Enter Patrons
        total_patrons = int(input("\nEnter the number of patrons: "))

        for i in range(total_patrons):
            print(f"\nEnter details for Patron {i + 1}")
            patron_no = input("Patron Number: ")
            patron_name = input("Patron Name: ")
            phone = input("Phone Number: ")

            self.patrons[patron_no] = {
                "name": patron_name,
                "phone": phone
            }

            self.borrowed[patron_no] = []

    # Borrow Book
    def borrow_book(self):
        patron_no = input("Enter Patron Number: ")

        if patron_no not in self.patrons:
            print("Patron not found.")
            return

        book_no = input("Enter Book Number: ")

        if book_no not in self.books:
            print("Book not found.")
            return

        if self.books[book_no]["quantity"] == 0:
            print("Book is not available.")
            return

        self.books[book_no]["quantity"] -= 1
        self.borrowed[patron_no].append(book_no)

        print(f"\n{self.patrons[patron_no]['name']} borrowed '{self.books[book_no]['name']}' successfully.")

    # Return Book
    def return_book(self):
        patron_no = input("Enter Patron Number: ")

        if patron_no not in self.patrons:
            print("Patron not found.")
            return

        book_no = input("Enter Book Number: ")

        if book_no in self.borrowed[patron_no]:
            self.borrowed[patron_no].remove(book_no)
            self.books[book_no]["quantity"] += 1
            print("Book returned successfully.")
        else:
            print("This patron has not borrowed this book.")

    # Display Books
    def display_books(self):
        print("\n========== BOOK LIST ==========")

        if not self.books:
            print("No books available.")
            return

        for book_no, details in self.books.items():
            status = "Available" if details["quantity"] > 0 else "Borrowed"

            print("Book Number :", book_no)
            print("Book Name   :", details["name"])
            print("Status      :", status)
            print("-" * 30)

    # Display Patrons
    def display_patrons(self):
        print("\n========== PATRON LIST ==========")

        if not self.patrons:
            print("No patrons registered.")
            return

        for patron_no, details in self.patrons.items():
            print("Patron Number :", patron_no)
            print("Name          :", details["name"])
            print("Phone Number  :", details["phone"])

            print("Borrowed Books:")
            if self.borrowed[patron_no]:
                for book in self.borrowed[patron_no]:
                    print(f"  {book} - {self.books[book]['name']}")
            else:
                print("  None")

            print("-" * 30)


# ---------------- MAIN PROGRAM ----------------

library = Library()

while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Display Books")
    print("4. Display Patrons")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.borrow_book()

    elif choice == "2":
        library.return_book()

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        library.display_patrons()

    elif choice == "5":
        print("\nThank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
