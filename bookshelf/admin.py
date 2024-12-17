# bookshelf/admin.py

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    list_filter = ('publication_year',)  # Add a filter by publication year
    search_fields = ('title', 'author')  # Enable search by title and author

# Register the Book model with the customized admin interface
admin.site.register(Book, BookAdmin)
