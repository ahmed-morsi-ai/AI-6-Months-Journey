class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  
        print(f"New Book Added: '{self.title}' by {self.author}")

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(f"You have returned '{self.title}'.")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

book1.borrow()
book1.borrow() 
book1.return_book()