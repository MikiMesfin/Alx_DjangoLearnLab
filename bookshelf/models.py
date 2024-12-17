from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=100, db_index=True)
    publication_year = models.IntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(timezone.now().year)
        ]
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title', 'author']),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"

    def clean(self):
        if self.publication_year > timezone.now().year:
            raise ValidationError('Publication year cannot be in the future')
        return super().clean()
