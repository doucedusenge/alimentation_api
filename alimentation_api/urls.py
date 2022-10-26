
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alimentation/',include('alimentation.urls')),
    path('chat/', include('chat.urls')),
]
