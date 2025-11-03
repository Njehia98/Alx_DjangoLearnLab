from relationship_app.models import Author, Book, Library, Librarian

# --- SAMPLE DATA CREATION (Run once) ---
def setup_sample_data():
    # Create an author
    author = Author.objects.create(name="George Orwell")

    # Create books
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)

    # Create a library and add books
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    # Create a librarian for the library
    Librarian.objects.create(name="Jane Doe", library=library)


# --- SAMPLE QUERIES ---

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books


# 2. List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


# --- DEMONSTRATION (Uncomment to run inside Django shell) ---
# setup_sample_data()
# print(get_books_by_author("George Orwell"))
# print(get_books_in_library("Central Library"))
# print(get_librarian_for_library("Central Library"))
