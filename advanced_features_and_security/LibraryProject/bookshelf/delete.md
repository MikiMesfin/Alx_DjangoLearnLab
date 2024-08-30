# delete.md

# Command:
from bookshelf.models import Book

retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()

# Verify deletion:
all_books = Book.objects.all()
print(all_books)

# Expected Output:
# <QuerySet []>  # The book has been successfully deleted.
