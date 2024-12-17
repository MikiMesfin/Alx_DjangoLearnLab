from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from bookshelf.models import Book

class BookViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2020,
            isbn="1234567890123"
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('bookshelf:book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookshelf/book_list.html')
        self.assertContains(response, "Test Book")

    def test_book_detail_view(self):
        response = self.client.get(reverse('bookshelf:book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookshelf/book_detail.html')
        self.assertContains(response, "Test Book")
        self.assertContains(response, "Test Author")

    def test_book_create_view(self):
        # Test unauthorized access
        response = self.client.get(reverse('bookshelf:book-create'))
        self.assertEqual(response.status_code, 302)  # Redirects to login

        # Test authorized access
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('bookshelf:book-create'))
        self.assertEqual(response.status_code, 200)

        # Test creating a book
        response = self.client.post(reverse('bookshelf:book-create'), {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2020,
            'isbn': '9876543210123'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertTrue(Book.objects.filter(title='New Book').exists())

    def test_book_update_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('bookshelf:book-update', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

        # Test updating a book
        response = self.client.post(reverse('bookshelf:book-update', args=[self.book.id]), {
            'title': 'Updated Book',
            'author': self.book.author,
            'publication_year': self.book.publication_year,
            'isbn': self.book.isbn
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_book_delete_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('bookshelf:book-delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

        # Test deleting a book
        response = self.client.post(reverse('bookshelf:book-delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists()) 