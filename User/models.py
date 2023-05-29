from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(('email address'), unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=200)
    age = models.CharField(max_length=3)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    JOB_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    job = models.CharField(max_length=10, choices=JOB_CHOICES)
    speciality = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    

    def __str__(self):
        return self.username
    

    # class Meta:
    #    abstract = True








    
