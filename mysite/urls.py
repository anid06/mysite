from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),# panel administratorski
    path('polls/',include('polls.urls')), #dołączamy plik urls z polls

]
