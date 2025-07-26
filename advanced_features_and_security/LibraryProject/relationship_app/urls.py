from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView 
 
# relationship_app.views import LibraryDetailView, RegisterView

urlpatterns = [
    path("book/", views.book_view, name="book"),
    path("library/<int:pk>", views.LibraryDetailView.as_view(), name="library"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("", views.index, name="index"),
    # Role based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    path("add_book/", views.can_add_book_view, name='can_add_book_view'),
    path("edit_book/", views.can_change_book_view, name='can_change_book_view'),
    path("can_delete_book_view/", views.can_delete_book_view, name='can_delete_book_view'),
]