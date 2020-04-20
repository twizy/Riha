from django.urls import path
from Apps.Locations.views import *

urlpatterns = [
    path('d/', AddDistrict),
    path('a/', AddArea),
    path('c/', AddCity),
    path('p/', AddProvince),
]