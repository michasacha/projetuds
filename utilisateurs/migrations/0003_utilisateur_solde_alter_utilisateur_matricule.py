# Generated by Django 5.0.6 on 2024-07-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0002_remove_utilisateur_is_gerant'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='solde',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='matricule',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
