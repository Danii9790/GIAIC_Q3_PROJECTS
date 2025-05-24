"""
Assignment: 11
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

"""

class Book:
    total_book = 0
    @classmethod
    def increment_book_count(cls):
        cls.total_book +=1

Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()

print(Book.total_book)
