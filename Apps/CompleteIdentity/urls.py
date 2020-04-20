from django.urls import path
from Apps.CompleteIdentity.views import *

urlpatterns = [
    path('pr/', AddCompleteIdentity),
]