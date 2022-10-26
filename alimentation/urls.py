
from tkinter import ROUND
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView , TokenObtainPairView


router= routers.DefaultRouter()
router.register("magasinier",MagasinierViewSet)
router.register("produit",ProduitViewSet)
router.register("commande",CommandeViewSet)
router.register("client",ClientViewSet)
router.register("vente",VenteViewSet)
router.register("userprofile",UserProfileViewSet)
router.register("users",UserViewSet)
router.register('Facturation',FacturationViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('alimentation_auth', include('rest_framework.urls')),
    path('login/',TokenPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view())    


    
]