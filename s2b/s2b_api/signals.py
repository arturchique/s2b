from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Worker


def create_user_profile(sender, instance, created, **kwargs):
    # Automatically creates a UserProfile on User creation.
    if created:
        Worker.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)