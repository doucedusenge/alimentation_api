from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.PROTECT,blank=True)
    adresse=models.CharField(max_length=100)
    date=models.DateField(auto_now=True,editable=False)
   
    def __str__(self) :
        return f"{self.user}" 

class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom_produit=models.CharField(max_length=50)
    prix=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now=True,editable=False)
    quantite=models.PositiveIntegerField(default=0,null=True)

    def __str__(self) -> str:
        return f"nom_produit: {self.nom_produit}"
class Magasinier(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)

class Vente(models.Model):
    id=models.BigAutoField(primary_key=True)    
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE,null=True)
    quantite=models.PositiveIntegerField(default=0,null=True)
    prix=models.PositiveIntegerField(default=0,null=True)
    date=models.DateTimeField(auto_now=True,editable=False)

    def __str__(self) -> str:
        return f"nom_produit: {self.produit}"

class Commande(models.Model):
    id=models.AutoField(primary_key=True)
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    quanti=models.PositiveIntegerField(default=0,null=True)
    prix=models.PositiveIntegerField(default=0,null=True)
    date=models.DateTimeField(auto_now=True,editable=False)
    
class Client(models.Model):
    id_client=models.AutoField(primary_key=True)
    nom_du_client=models.CharField(max_length=50)
    prenom_du_client=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)

class Date(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(auto_now=False)    

      
    
   



