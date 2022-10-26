from tkinter import ROUND
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView , TokenObtainPairView
from . import views
from django.urls import path


router= routers.DefaultRouter()
router.register("message",MessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('chat_auth', include('rest_framework.urls')),
        # URL form : "/api/messages/1/2"
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # URL form : "/api/messages/"
    path('api/messages/', views.message_list, name='message-list'),   # For POST
    # URL form "/api/users/1"
    path('api/users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
    path('api/users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
  
]