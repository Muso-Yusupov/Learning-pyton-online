class Book:
    def __init__(self,name,author,p_year):###p_year is published of the Book
        self.name = name
        self.author = author
        self.p_year = p_year
    def get_name(self):
        return self.name
    def get_author(self):
        return self.author
    def get_p_year(self):
        return self.p_year
    
class Library:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.books = []
    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_books(self):
        return [f"{self.name},{self.location}"]
    def add_book(self,book):
        self.books.append(book)
    def get_info(self):
        a = [f"{c.get_author()} {c.get_name()}" for c in self.books]
        print(f"{self.name} in which location in {self.location} has these: {', '.join(a)}")
        


book1 = Book("Start with why","Arthur",1990)
library1 = Library("Central Library","Tashkent")

library1.add_book(book1)
library1.get_info()