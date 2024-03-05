class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __eq__(self, other):
        return (self.title == other.title) and (self.author == other.author)

    def __ne__(self, other):
        return (self.title != other.title) or (self.author != other.author)


book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")

print(book1 == book2)
print(book1 != book2)
