from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Compte


 
     
    
admin.site.site_header = ("UDS-Resto Administration")
admin.site.site_title = ("UDS-Resto Admin Portal")
admin.site.index_title = ("Welcome to UDS-Resto Admin")
admin.site.register(Compte)
 

# Register your models here.
