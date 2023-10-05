class Book:
    def __init__(self,title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability
    
    def borrow(self):
        if(self.availability == False):
            print("Book is not available, Please wait for its availabililty")
        else:
            print("Book is issued collect it from library")
            self.availability = False
    def book_return(self):
        print("Thanks for returning the book")
        self.availability = True    

book1 = Book("Artificial intelligence", "Richi", False)
print(book1.borrow())


        