import os
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete
from .models import Utilisateur  # Remplace par le nom de ton modèle

@receiver(pre_save, sender=Utilisateur)  # Assure-toi de remplacer UserProfile par le nom de ton modèle
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_instance = sender.objects.get(pk=instance.pk)  # Récupère l'ancienne instance du modèle
    except sender.DoesNotExist:
        return False
    
    if instance.profil_photo and (not old_instance.profil_photo == instance.profil_photo or old_instance.profil_photo is None):
        if old_instance.profil_photo and os.path.isfile(old_instance.profil_photo.path):
            os.remove(old_instance.profil_photo.path)  # Supprime l'ancienne image du système de fichiers

# définir une fonction qui supprime le fichier de la photo de profil
@receiver(post_delete, sender=Utilisateur)
def supprimer_photo(sender, instance, **kwargs):
    # vérifier si l'utilisateur a une photo de profil
    if instance.profil_photo:
        # construire le chemin du fichier
        fichier = os.path.join(settings.MEDIA_ROOT, instance.profil_photo.name)
        # supprimer le fichier s'il existe
        if os.path.isfile(fichier):
            os.remove(fichier)