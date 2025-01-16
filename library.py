

class Book:
    def __init__(self,title,author,pages,is_aviable=True):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_aviable = is_aviable
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append({
            "title":book.title,
            "author":book.author,
            "pages":book.pages,
            "is_aviable":book.is_aviable
        })

    # Вернет список доступных книг
    def show_available_books(self):
        find_available_books = lambda book: book["is_aviable"] == True
        available_books = list(filter(find_available_books,self.books))

        return available_books
    
    # Ищем книгу
    def borrow_book(self,book_title):
        find_book = lambda book : book["title"] == book_title
        book = list(filter(find_book,self.books))
        
        if book:
            book = book[0]
            if book in self.show_available_books(): # Если доступно
                self.books[self.books.index(book)]["is_aviable"] = False # Меняем стату на недоступно
                return book 
            else: 
                return f"Книга {book["title"]} не деступно"
            
        return None


book1 = Book("Гарри Поттер","Дж.К. Роулинг",500,)
library = Library()

library.add_book(book1)
print(library.show_available_books())
print(library.borrow_book(book1.title))
print(library.borrow_book(book1.title))