"""
URL configuration for projetuds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#from comptes.views import  CompteDetailView, DepositView, WithdrawView
from utilisateurs.views import CustomUserCreateView
from django.urls import path
from comptes.views import DepotView, RetraitView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('users/create/', CustomUserCreateView.as_view(), name='user-create'),
    path('comptes/<int:pk>/depot/', DepotView.as_view(), name='compte-depot'),
    path('comptes/<int:pk>/retrait/', RetraitView.as_view(), name='compte-retrait'),
]


 
    


 


 