class Book:
    def __init__(self, book_name, book_author, book_year):
        self.name = book_name
        self.author = book_author
        self.year = book_year

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author and self.year == other.year