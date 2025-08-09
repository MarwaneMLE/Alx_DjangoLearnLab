from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    # Meta class defines which model and fields to include in the serialization
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]  # Serializing all key fields

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year  # Get current year

        # If publication year is greater than current year, raise an error
        if value > current_year:
            raise serializers.ValidationError("Publication year can't be in the future")
        
        return value  # Return the valid value if no error


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nesting BookSerializer to dynamically include related books
    books = BookSerializer(many=True, read_only=True)  # Many books per author, read-only

    class Meta:
        model = Author
        fields = ["name", "books"]  # Include author's name and related books
