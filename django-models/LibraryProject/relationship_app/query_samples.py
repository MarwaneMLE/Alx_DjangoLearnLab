import os
import sys
import django

# 🔧 Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

# ✅ Import models
from relationship_app.models import Author, Book, Library, Librarian
 
# Query 1: Get all books written by a specific author (e.g., George Orwell)
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")




"""
# 1️⃣ Query all books by a specific author
author_name = "Jane Austen"
try:
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using related_name="books"
    print(f"\n📚 Books by {author.name}:")
    for book in books:
        print(f" - {book.title}")
except Author.DoesNotExist:
    print(f"\n❌ No author found with name '{author_name}'.")

# 2️⃣ List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using related_name="books" on the Library model
    print(f"\n🏛️ Books in '{library.name}':")
    for book in books:
        print(f" - {book.title}")
except Library.DoesNotExist:
    print(f"\n❌ No library found with name '{library_name}'.")

# 3️⃣ Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\n👤 Librarian of '{library_name}': {librarian.name}")
except Librarian.DoesNotExist:
    print(f"\n❌ No librarian assigned to '{library_name}'.")
"""