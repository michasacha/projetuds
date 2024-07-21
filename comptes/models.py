from django.db import models
from utilisateurs.models import Utilisateur
from django.core.exceptions import ValidationError

class Compte(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    solde = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - solde: {self.solde}"

    def depot(self, montant):
        if montant <= 100:
            raise ValidationError("Le montant du dépôt doit être supérieur à cent.")
        self.solde += montant
        self.save()

    def retrait(self, montant):
        if montant <=   100:
            raise ValidationError("Le montant du retrait doit être supérieur à cent.")
        if self.solde < montant:
            raise ValidationError("Fonds insuffisants pour le retrait.")
        self.solde -= montant
        self.save()
