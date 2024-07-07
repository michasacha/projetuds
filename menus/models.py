from django.db import models

class Repas(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='repass_photos/')
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    date = models.DateField(unique=True)
    repas = models.ForeignKey(Repas, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.date} - {self.repas.name}"

