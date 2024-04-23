class Book:
    def __init__(self, book_id, title, author, shelf_location="", status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.shelf_location = shelf_location
        self.status = status

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_shelf_location(self):
        return self.shelf_location

    def set_shelf_location(self, new_location):
        self.shelf_location = new_location

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status

def search_book(book_list, keyword):
    found_books = []
    for book in book_list:
        if keyword.lower() in book.get_title().lower() or keyword.lower() in book.get_author().lower():
            found_books.append(book)
    return found_books

if __name__ == "__main__":

    books = [
        Book("B001", "Pemrograman Berorientasi Objek", "Yonathan Dea", "A3"),
        Book("B002", "Data Science Handbook", "Jane Doe", "B2"),
        Book("B003", "Machine Learning Basics", "John Smith", "C5"),
        Book("B004", "Java Programming", "Alice Johnson", "D1")
    ]

    keyword = "Pemrograman"

    search_result = search_book(books, keyword)

    if search_result:
        print("Search Results:")
        for book in search_result:
            print("Book ID:", book.get_book_id())
            print("Title:", book.get_title())
            print("Author:", book.get_author())
            print("Shelf Location:", book.get_shelf_location())
            print("Status:", book.get_status())
            print()
    else:
        print("No books found matching the search criteria.")