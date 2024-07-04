class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'
        
class Library:
    def __init__(self) -> None:
        self.books = []

    def get_book(self, book):
        self.books.append(f'Книга "{book.title}" добавлена в библиотеку.')

    def del_book(self):
        for book in self.books:
            self.books.remove(book)
            print(f'Book {self.title} removed ')


l = Library()

a = Book('Python', 'Ruslan')
l.get_book(a)

