
from django.contrib import admin
from .models import *

admin.site.register(Produit)
admin.site.register(Magasinier)
admin.site.register(Commande)
admin.site.register(Client)
admin.site.register(Vente)

# Register your models here.
