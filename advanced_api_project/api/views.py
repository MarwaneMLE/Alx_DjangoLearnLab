from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers
from django_filters import rest_framework
from rest_framework import filters

# View to list all books with filtering, search, and ordering capabilities
class BookListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]  # Require token-based authentication
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access to unauthenticated users; restrict write access

    serializer_class = BookSerializer  # Use BookSerializer to serialize book data
    queryset = Book.objects.all()  # Fetch all books from the database

    # Enable filtering by title, author, or publication year
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']

    # Enable search on title and author fields
    filter_backends += [filters.SearchFilter]
    search_fields = ['title', 'author__name']  # Use author__name to search through related field

    # Enable ordering by title or publication year
    filter_backends += [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']


# View to retrieve a single book using its ID
class BookRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]  # Token auth required
    permission_classes = [IsAuthenticatedOrReadOnly]  # Public read access allowed
    queryset = Book.objects.all()  # Books to query from
    serializer_class = BookSerializer  # Use BookSerializer


# View to create a new book (POST request)
class BookCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]  # Require authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Custom logic to prevent creating a book with a duplicate title
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError(f'Book with title "{title}" already exists')
        else:
            serializer.save()  # Save the new book


# View to update an existing book (PUT/PATCH request)
class BookUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]  # Require authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Custom validation: prevent setting the title to an empty string
    def perform_update(self, serializer):
        title = serializer.validated_data.get('title', '')
        if len(title.strip()) == 0:
            raise serializers.ValidationError('Title cannot be empty')
        else:
            serializer.save()  # Apply the update


# View to delete a book by ID
class BookDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]  # Require authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Delete the selected book instance
    def perform_destroy(self, instance):
        instance.delete()
