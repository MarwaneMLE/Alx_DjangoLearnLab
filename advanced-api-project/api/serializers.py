from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested representation of the author's books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

