from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.conf import settings
# import os

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
           """
              Creates and return a regular user with the given email and password
           
           """
           
           if not email:
               raise ValueError('The email field must be provided.')
           
           email = self.normalize_email(email)
           extra_fields.setdefault('is_active', True)
           
           # User instance
           user = self.model(email=email, **extra_fields)
           
           if password:
                user.set_password(password)
           user.save(using=self._db)
           return user
       
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, **extra_fields)
    
 # User model     
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    
    objects = CustomUserManager()
    
    # Email as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
    
    
# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/',  blank=True, null=True)
    
    # Custom profile picture cleanup
    # def save(self, *args, **kwargs):
    #     # Delete old profile picture if updating
    #     if self.pk:
    #         old_profile = Profile.objects.filter(pk=self.pk).first()
    #         if old_profile and old_profile.profile_picture != self.profile_picture:
    #             old_profile.profile_picture.delete(save=False)
    #     super().save(*args, **kwargs)
        
    # def delete(self, *args, **kwargs): 
    #     # Delete the associated profile picture when the Profile is deleted
    #     if self.profile_picture:
    #         self.profile_picture.delete(save=False)
    #     super().delete(*args, **kwargs)               
    
    def __str__(self):
        return f'Profile of {self.user.email}'    
