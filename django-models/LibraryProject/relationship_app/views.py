from django.shortcuts import render, redirect
from relationship_app.models import Author, Book, Librarian, Library
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required

# Create your views here.
def book_view(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context=context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object() 
        context = {"library": library}

        #context["books_list"] = library.get_books_list()
        return context


# =============== Authentifiction Views ===============
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.http import request
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# User login view
class LoginView(LoginView):
    template_name = "login.html"
    #success_url = '/logout/'

# User logout view
class LogoutView(LogoutView):
    template_name = "logout.html" 
   

#Homepage View
def index(request):
    return render(request, "relationship_app/index.html")

#Setting Up Role-Based Views
#Checks if user is Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

#Checks if user is Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#Checks if user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

#Views to Enforce Permissions
@permission_required("relationship_app.can_add_book")
def can_add_book_view(request):
    return render(request, 'relationship_app/can_add_book.html')

@permission_required("relationship_app.can_change_book")
def can_change_book_view(request):
    return render(request, 'relationship_app/can_change_book.html')

@permission_required("relationship_app.can_delete_book")
def can_delete_book_view(request):
    return render(request, 'relationship_app/can_delete_book.html')