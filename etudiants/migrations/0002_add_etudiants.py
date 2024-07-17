# etudiants/migrations/0002_add_etudiants.py
from django.db import migrations

def add_etudiants(apps, schema_editor):
    Etudiant = apps.get_model('etudiants', 'Etudiant')
    etudiants = [
        {'matricule': 'CM-UDS-21SCI1625', 'nom': 'GUIADEM KOUAM', 'prenom':'MICHELE SACHA' },
        {'matricule': 'CM-UDS-20SCI0130', 'nom': 'LEMONANG NGUIMATIO', 'prenom': 'BRAY'},
        {'matricule': 'CM-UDS-23SCI1421', 'nom': 'DOUNLA DJITOUO', 'prenom': 'SIMON'},
        {'matricule': 'CM-UDS-20SCI0207', 'nom': 'CHEBOU POKA', 'prenom': 'DAÏNA AGUY'},
        {'matricule': 'CM-UDS-21SCI1686', 'nom': 'ZANGUE NGUEABOU', 'prenom': 'CLASVIN'},
        {'matricule': 'CM-UDS-19SCI1040', 'nom': 'NJOYA MOULIEM', 'prenom': 'GERMAIN JUNIOR'},
        {'matricule': 'CM-UDS-20SCI0729', 'nom': 'TEUBOU TALLA', 'prenom': 'MIRABELLE'},
        {'matricule': 'CM-UDS-23SCI1427', 'nom': 'KAMGA KAMMAGNE', 'prenom': 'BRICE'},
        {'matricule': 'CM-UDS-19SCI1127', 'nom': 'SAFANG', 'prenom': 'ARMAND'},
        {'matricule': 'CM-UDS-23SCI1428', 'nom': 'KEABOU KONNANG', 'prenom': 'ASERNE R.'},
        
    ]
     
    for etudiant_data in etudiants:
        Etudiant.objects.create(**etudiant_data)

class Migration(migrations.Migration):

    dependencies = [
        ('etudiants', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_etudiants),
    ]
