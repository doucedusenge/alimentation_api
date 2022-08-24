from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from rest_framework.authentication import SessionAuthentication

from .models import *

# Create your views here.

class ProduitViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Produit.objects.all()
    serializer_class=ProduitSerializer
class MagasinierViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Magasinier.objects.all()
    serializer_class=MagasinierSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset= Commande.objects.all()
    serializer_class=CommandeSerializer

class VenteViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Vente.objects.all()
    serializer_class=VenteSerializer      
    
class ClientViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Client.objects.all()
    serializer_class=ClientSerializer   