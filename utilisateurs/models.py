from django.contrib.auth.models import AbstractUser
from django.db import models 

class Utilisateur(AbstractUser):
   date_of_birth = models.DateField(null=True, blank=True)
   phone_number = models.CharField(max_length=15, blank=True)
   matricule = models.CharField(max_length=15, blank=False)
   profil_photo= models.ImageField(upload_to='profil_photos/', blank=True, null=True)
   is_prof = models.BooleanField(default=False)

# Create your models here.
