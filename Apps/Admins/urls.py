from django.urls import path
from Apps.Admins.views import *

urlpatterns = [
    path('attr/',attribute,name='attr'),
]