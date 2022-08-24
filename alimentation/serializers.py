from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produit
        fields="__all__"

class MagasinierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Magasinier
        fields="__all__"

class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vente
        fields="__all__"

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Commande
        fields="__all__"  
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__"                    