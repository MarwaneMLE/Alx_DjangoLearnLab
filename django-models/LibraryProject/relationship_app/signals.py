from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


# Create a profile when a new user sign up
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

post_save.connect(create_user_profile, sender=User)

