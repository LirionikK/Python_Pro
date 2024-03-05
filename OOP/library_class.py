class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class Library:
    def __init__(self, books_list) -> None:
        self.books_list = books_list

    def __len__(self):
        return len(self.books_list)

    def __getitem__(self, index):
        return self.books_list[index]


b1 = Book("Title1", "Author1")
b2 = Book("Title2", "Author2")
b3 = Book("Title3", "Author3")

library = Library([b1, b2, b3])
print(len(library))
print(library[2])
