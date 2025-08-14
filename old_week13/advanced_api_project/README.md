📚 View Configuration Summary

🔹 BookListView
Purpose: Retrieves and displays a list of all books.

Authentication: Uses TokenAuthentication.

Permissions: IsAuthenticatedOrReadOnly — allows any user (authenticated or not) to view the list, but restricts write actions to authenticated users.

Features: Supports filtering, searching, and ordering of books.

🔹 BookDetailView
Purpose: Retrieves a single book by its ID.

Authentication: Uses TokenAuthentication.

Permissions: IsAuthenticatedOrReadOnly — both authenticated and unauthenticated users can view book details.

Features: Simple read-only view for individual book retrieval.

🔹 BookCreateView
Purpose: Allows creation of a new book.

Authentication: Uses TokenAuthentication.

Permissions: IsAuthenticated — only logged-in users can create books.

Customization: Overrides perform_create to check if a book with the same title already exists. If it does, a ValidationError is raised to prevent duplication.

🔹 BookUpdateView
Purpose: Updates the details of an existing book.

Authentication: Uses TokenAuthentication.

Permissions: IsAuthenticated — only authenticated users can modify book data.

Customization: Overrides perform_update to ensure the title field is not empty. If it is, a ValidationError is raised to enforce valid input.

🔹 BookDeleteView
Purpose: Deletes a book from the database.

Authentication: Uses TokenAuthentication.

Permissions: IsAuthenticated — only authenticated users are allowed to delete books.

Customization: Inherits default perform_destroy behavior from DestroyAPIView to handle deletion without additional logic.
