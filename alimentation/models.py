from django.db import models

# Create your models here.


class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom_produit=models.CharField(max_length=50)
    prix=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now=True,editable=False)
    quantite=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"nom_produit: {self.nom_produit} "


class Magasinier(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)

class Vente(models.Model):
    id_vente=models.AutoField(primary_key=True)    
    produit=models.CharField(max_length=50)
    quantite=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now=True,editable=False)

class Commande(models.Model):
    id=models.AutoField(primary_key=True)
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    quanti=models.CharField(max_length=50,null=True)
    
class Client(models.Model):
    id_client=models.AutoField(primary_key=True)
    nom_du_client=models.CharField(max_length=50)
    prenom_du_client=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)
    
   



