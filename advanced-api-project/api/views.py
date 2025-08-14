# Import permission classes to control access
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Import generic class-based views and filters
from rest_framework import generics, filters

# Import serializers and models
from .serializers import BookSerializer
from .models import Book, Author

# Import filter backends
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters


# Filter class for searching/filtering books by title, author, or publication year
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search by title
    author = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search by author
    publication_year = django_filters.NumberFilter(field_name='publication_year')  # Exact match

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# View for creating new books (only for authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def create(self, serializer):
        # Get or create an author from request data ( 
        author = self.request.data.get('Dan Brown') 
        author = Author.objects.get_or_create(name=author)[0]
        serializer.save(author=author)

# View for listing all books with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = BookFilter  # Uncomment to enable advanced filtering
    ordering_fields = ['title', 'publication_year']  # Fields that can be ordered
    search_fields = ['title', 'author']  # Fields that can be searched
    ordering = ['title']  # Default ordering

# View for retrieving a single book by ID (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# View for updating a book (only for authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# View for deleting a book (only for authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
