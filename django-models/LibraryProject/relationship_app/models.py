from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver  
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    PERMISSION_CHOICES = (
        ('can_add_book', 'Can Add Book'),
        ('can_change_book', 'Can Change Book'),
        ('can_delete_book', 'Can Delete Book'),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="author")
    permission = models.CharField(max_length=50, choices=PERMISSION_CHOICES, default='can_add_book')
    meta_description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.permission})"

    class Meta:
        verbose_name = "Book"


"""class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return f"{self.title} by {self.author}"
     
    #Extending Book Model with Custom Permissions
    class Meta:
        Permissions_Choices =(
            ('can_add_book', 'can_add_book'),
            ('can_change_book', 'can_change_book'),
            ('can_delete_book', 'can_delete_book'),
        )

    permissions = models.CharField(max_length=50,  choices="Permissions_Choices")
    meta = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} - {self.permissions}"""


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarians")

    def __str__(self):
        return f"{self.library.name} - Librarian."


#Extending User Model with a UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    RoleChoices =(
        ('Admin','Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

role = models.CharField(max_length=50,  choices='RoleChoices')
userprofile = models.TextField()


def __str__(self):
    return f"{self.user.username} - {self.role}"


#Signal to automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


 