from ast import Delete
import email
from gc import get_objects
from pickle import PUT
from traceback import print_tb
from webbrowser import get
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets ,mixins
from rest_framework.views import APIView
from django.contrib.auth.models import User ,Group
from .serializers import *
from .models import *


class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer

class GroupViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = IsAuthenticated,
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-id')
    @transaction.atomic()
    def update(self,request,pk):
        user = self.get_object()
        print(user)
        data = request.data
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        nouv_password = data.get('nouv_password')
        anc_password = data.get('anc_password')
        if user.check_password(anc_password):
            print("checked")
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(nouv_password)
            user.save()
            return Response({"status":"Utilisateur modifié avec success"},201)
        return Response({"status":"Ancien mot de passe incorrect"},400)


class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = IsAuthenticated,
    serializer_class = UserProfileSerializer
    queryset =  UserProfile.objects.all().order_by('-id')

    @transaction.atomic()
    def create(self,request):
        data = request.data
        print(data)
        groupe=data.get('user.groups')
        user = User(
            username = data.get('user.username'),
            first_name = data.get('user.first_name'),
            last_name = data.get('user.last_name'),
            email=data.get('user.email')
        )
        
        user.set_password(data.get('user.password'))
        user.save()

        print(user.password)
        user.groups.add(groupe[0])
    
        userprofile = UserProfile(
            user = user,
            adresse=data.get('adresse'),
            )
        userprofile.save()
        serializer =UserProfileSerializer(userprofile,many=False).data
        return Response(serializer,201)

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
   

    @action(detail=False,methods=['get'],url_path=r'commande',url_name=r'commande')
    def get_commande(self,request):
        Commandes=Commande.objects.filter(prix__gte=0).aggregate(Sum("prix")).get('prix__sum')
        return Response({"la somme des commandes":Commandes})

    def create(self, request):
        data=request.data
        print(data)
        produit_obj=Produit.objects.get(id=data["produit"])
        commande_obj=Commande(
            produit=produit_obj,
            prix=int(data["prix"]),
            quanti=int(data["quanti"])
        )
        #commande_obj.prix*=int(data["quanti"])
        commande_obj.save()
        produit_obj.quantite +=int(data["quanti"])
        produit_obj.save()
        return Response(200)    

class VenteViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Vente.objects.all()
    serializer_class=VenteSerializer  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']
    
    
    def get_queryset(self):
        queryset= Vente.objects.all().order_by("id")
        du= self.request.query_params.get('du')
        au= self.request.query_params.get('au')
        if du is not None:
            queryset= queryset.filter(date__gte=du, date__lte=au)
        return queryset

    @action(detail=False,methods=['get'],url_path=r"tot_vente",url_name=r'tot_vente')
    def get_vente(self,request):
        #x = Vente.objects.filter(prix__gte=0)
        #print(x)
        ventes=Vente.objects.filter(prix__gte=0).aggregate(Sum("prix")).get("prix__sum")
        #start_date=datetime(2022,9,2)
        #end_date=datetime(2022,9,9)
       # new= Vente.objects.filter(date__range=[start_date,end_date]).aggregate(Sum("prix")).get("prix__sum")
        #print(new)
        return  Response({"total_ventes":ventes },200)

    #@action(detail=False,methods=['get'],url_path=r"total",url_name=r'total')
    #def get_queryset(self):
        #start_date = datetime.date.today()
        #end_date = start_date + datetime.timedelta(days=6)
        #time_filter = self.queryset.filter(date__range=(start_date, end_date))
        #ser = VenteSerializer(time_filter, many=True).data
        #return ser
        
    @action(detail=False,methods=['get'],url_path=r"vente",url_name=r"vente")
    def get_benefice(self,request):
        benefices_tab_com=[]
        benefices_tab_v=[]    
        produit=Produit.objects.filter(prix__gte=0)
        somme=0
        for p in produit:
            ventes_prix = Vente.objects.filter(produit=p).aggregate(Sum("prix")).get("prix__sum")
            commandes_prix = Commande.objects.filter(produit=p).aggregate(Sum("prix")).get("prix__sum")
            benefices_tab_com.append(commandes_prix)
            benefices_tab_v.append(ventes_prix)
            if(ventes_prix is  not None and commandes_prix is not None):
                benefices_tab_v.append((ventes_prix-commandes_prix))
        for x in benefices_tab_v:
            if(x):
                somme+=x
        #startDate=datetime(2022,8,31)
        #endDate=datetime(2022,9,9)
        #new=Vente.objects.filter(date__range=[startDate,endDate]).aggregate(Sum("prix")).get("prix__sum")

        return Response({"Benefice":somme},200)   

    #def get_date(self):
       # time_filter = self.queryset.objects.filter(DateTimeField__gte=<some_date>, DateTimeField__lte=<some date>)
       # return time_filter

    def create(self,request):
        data=request.data
        print(data)
        produit_obj=Produit.objects.get(id=data["produit"])
        vente_obj=Vente(
            produit=produit_obj,
            prix=int(data["prix"]),
            quantite=int(data["quantite"])
        )
        vente_obj.save()
        produit_obj.quantite -=int(data["quantite"])
        produit_obj.save()
        return Response(200)

class ClientViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Client.objects.all()
    serializer_class=ClientSerializer   

class DateViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Date.objects.all()
    serializer_class=DateSerializer
