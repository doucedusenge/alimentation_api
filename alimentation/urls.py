
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import *

router= routers.DefaultRouter()
router.register("magasinier",MagasinierViewSet)
router.register("produit",ProduitViewSet)
router.register("commande",CommandeViewSet)
router.register("client",ClientViewSet)
router.register("vente",VenteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('alimentation_auth', include('rest_framework.urls'))
    
]