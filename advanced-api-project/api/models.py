from django.db import models


# Model representing an author
class Author(models.Model):
    # Author's name with a max length of 50 characters
    name = models.CharField(max_length=50)

    def __str__(self):
        # String representation of the author (used in admin, shell, etc.)
        return f"{self.name}"


# Model representing a book
class Book(models.Model):
    # Book title with a max length of 100 characters
    title = models.CharField(max_length=100)

    # Publication year stored as a full date (you might consider using IntegerField for just the year)
    publication_year = models.DateField()

    # ForeignKey linking to Author
    # - on_delete=models.CASCADE means if the author is deleted, the related books will be deleted too
    # - related_name="books" allows accessing all books of an author via `author.books.all()`
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        # String representation of the book
        return f"{self.title}"
