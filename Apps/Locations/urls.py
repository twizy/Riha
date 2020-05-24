from django.urls import path
from Apps.Locations.views import *

urlpatterns = [
    path('d/', AddDistrict,name='d'),
    path('a/', AddArea,name='a'),
    path('c/', AddCity,name='c'),
    path('p/', AddProvince,name='p'),
    path('t/', TestingView,name='t'),
    path('v/', TestingViews,name='v'),
]