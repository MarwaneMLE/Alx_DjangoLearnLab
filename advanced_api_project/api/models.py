from django.db import models


# Author model: represents an individual author
class Author(models.Model):
    # Name of the author (required, must be unique)
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name  # Helpful for admin display and debugging


# Book model: represents a book written by an author
class Book(models.Model):
    # Title of the book (required, must be unique)
    title = models.CharField(max_length=100, blank=False, unique=True)

    # Year the book was published (required)
    publication_year = models.IntegerField(blank=False)

    # Foreign key to Author (each book is linked to one author)
    # on_delete=models.CASCADE means if the author is deleted, their books are also deleted
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title  # Helpful for admin display and debugging
