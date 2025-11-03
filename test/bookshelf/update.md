### Update Operation

```python
from bookshelf.models import Book

# Retrieve and update the book's title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book.title
