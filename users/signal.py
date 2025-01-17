from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Automatically creates or updates the Profile when a User instance is saved.
    """
    if created:
        # Create the profile when the user is created
        Profile.objects.create(user=instance)
    else:
        # Save the profile when the user is updated
        instance.profile.save()
