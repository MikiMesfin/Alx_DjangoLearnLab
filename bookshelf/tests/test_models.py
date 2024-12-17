from django.test import TestCase
from django.core.exceptions import ValidationError
from bookshelf.models import Book
from django.utils import timezone

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2020
        )

    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(self.book.__str__(), "Test Book by Test Author")

    def test_publication_year_validation(self):
        future_year = timezone.now().year + 1
        book = Book(
            title="Future Book",
            author="Future Author",
            publication_year=future_year
        )
        with self.assertRaises(ValidationError):
            book.full_clean() 