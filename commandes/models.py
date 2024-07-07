import menus
from menus.models import Menu
from django.db import models
from django.conf import settings
 


class Commande(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # Assume that you have a MenuItem model
    nombre_de_tickets = models.PositiveIntegerField()
    code_pin = models.CharField(max_length=4)  # You can use a more secure field depending on requirements
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
                                                                                                                                                                                                                    
    def __str__(self):
        return f"Commande {self.id} by {self.user}"
 
