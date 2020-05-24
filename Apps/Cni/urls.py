from django.urls import path
from Apps.Cni.views import *
from django.contrib.auth.models import User

urlpatterns = [
    path('p/', AddProfil, name='p'),
]