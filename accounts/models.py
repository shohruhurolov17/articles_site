from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=150)
    job = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default='Male'
    )



