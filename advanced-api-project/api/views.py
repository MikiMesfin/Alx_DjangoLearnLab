from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print("Creating a new book")
        serializer.save()

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    """
View for listing all books.
- GET: Retrieve a list of all books.
"""
"""
View for retrieving a single book by its ID.
- GET: Retrieve details of a specific book using its ID.
"""
"""
View for creating a new book.
- POST: Create a new book with the provided data.
"""
"""
Custom behavior before saving a new book.
"""
"""
View for updating an existing book.
- PUT: Update details of an existing book using its ID.
"""
"""
View for deleting a book.
- DELETE: Remove a book using its ID.
"""

