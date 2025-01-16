from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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
              
           else:
               raise ValueError('Password must be provided for the user.')   
           user.save(using=self._db)
           return user
       
    def create_superuser(self, email, password=None, **extra_fields):
        """"
           Create and return a superuser with the given email and password.
           
        """ 
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
    
      
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    
    objects = CustomUserManager()
    
    # Email as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
