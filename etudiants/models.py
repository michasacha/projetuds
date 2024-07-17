from django.db import models

class Etudiant(models.Model):
    matricule = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.matricule} - {self.nom} {self.prenom}"
