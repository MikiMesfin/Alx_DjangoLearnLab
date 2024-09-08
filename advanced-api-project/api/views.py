from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# List all books and allow authenticated users to create a new one.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly] 

    def perform_create(self, serializer):
        print("Creating a new book")
        serializer.save() 

# Retrieve, update, or delete a specific book by ID.
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly]  

    def perform_update(self, serializer):
        print("Updating book with ID:", self.get_object().id)
        serializer.save()

"""
BookListCreateView:
- GET: Lists all books (available to everyone).
- POST: Creates a new book (only for authenticated users).

BookRetrieveUpdateDestroyView:
- GET: Retrieves a specific book by ID.
- PUT: Updates the book (only for authenticated users).
- DELETE: Deletes the book (only for authenticated users).
"""
