from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisteur(AbstractUser):
    date_of_birth= models.DateField(null=True, blank=True)
    phone_number= models.CharField(max_length=15, blank=True)
    matricule= models.CharField(max_length=15, blank=False)
    profile_photo= models.ImageField(upload_to='profil_photos/', null=True, blank=True)
    sex= models.CharField(max_length=1, blank=False)
# Create your models here.
