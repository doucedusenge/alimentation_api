from django.shortcuts import render
from gc import get_objects
from pickle import PUT
from traceback import print_tb
from webbrowser import get
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MessageSerializer
from rest_framework.authentication import SessionAuthentication
from .models import *
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# Users View
@csrf_exempt                                                              # Decorator to make the view csrf excempt.
def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        if pk:                                                                      # If PrimaryKey (id) of the user is specified in the url
            users = User.objects.filter(id=pk)              # Select only that particular user
        else:
            users = User.objects.all()                             # Else get all user list
        serializer = UserSerializer(users, many=True, context={'request': request}) 
        return JsonResponse(serializer.data, safe=False)               # Return serialized data
    elif request.method == 'POST':
        data = JSONParser().parse(request)           # On POST, parse the request object to obtain the data in json
        serializer = UserSerializer(data=data)        # Seraialize the data
        if serializer.is_valid():
            serializer.save()                                            # Save it if valid
            return JsonResponse(serializer.data, status=201)     # Return back the data on success
        return JsonResponse(serializer.errors, status=400)  

@csrf_exempt
def message_list(request, sender=None, receiver=None):
            """
            List all required messages, or create a new message.
            """
            if request.method == 'GET':
                messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
                serializer = MessageSerializer(messages, many=True, context={'request': request})
                return JsonResponse(serializer.data, safe=False)
            elif request.method == 'POST':
                data = JSONParser().parse(request)
                serializer = MessageSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)


class MessageViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    