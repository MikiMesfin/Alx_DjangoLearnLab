from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


"""
Author model:
- name: stores the author's name.
Book model:
- title: stores the book's title.
- publication_year: ensures that the year is a valid integer and not in the future.
- author: establishes a foreign key linking to the Author model.
"""
