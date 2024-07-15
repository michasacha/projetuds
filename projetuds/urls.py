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
from commandes.views import CommandeCreateView
from utilisateurs.views import CustomUserCreateView
from comptes.views import DepotView, RetraitView
from menus.views import RepasListCreateAPIView, RepasRetrieveUpdateDestroyAPIView, MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('users/create/', CustomUserCreateView.as_view(), name='user-create'),
    path('comptes/<int:pk>/depot/', DepotView.as_view(), name='compte-depot'),
    path('comptes/<int:pk>/retrait/', RetraitView.as_view(), name='compte-retrait'),
    path('repass/', RepasListCreateAPIView.as_view(), name='repas-list-create'),
    path('repass/<int:pk>/', RepasRetrieveUpdateDestroyAPIView.as_view(), name='repas-detail'),
    path('menus/', MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyAPIView.as_view(), name='menu-detail'),
    path('commandes/', CommandeCreateView.as_view(), name='commande-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('etudiants.urls')),
]

 

 

 
    


 


 