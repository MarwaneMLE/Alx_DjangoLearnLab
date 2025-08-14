from rest_framework import serializers
from . models import Book, Author
from datetime import datetime

# Import the required modules
from rest_framework import serializers  # DRF serializer base classes
from datetime import datetime  # To get current year for validation
from .models import Book, Author  # Importing the models

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Book  # Specify the model to serialize
        fields = ["title", "publication_year", "author"]  # Fields to include in the output

    # Custom validator for the publication_year field
    def validate_publication(self, value):
        current_year = datetime.now().year  # Get the current year
        if value > current_year:
            # Raise error if year is in the future
            raise serializers.ValidationError("The publication year is greater than the current year")
        return value  # Return the valid year


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer): 
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author  # Specify the model to serialize
        fields = ["name", "books"]  # Include author's name and their books
