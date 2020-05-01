from django.urls import path
from Apps.Base.views import *
from Apps.CompleteIdentity.models import *

urlpatterns = [
    path('', Index,name='index'),
    path('cl/', CompleteIdentityList, name='cl'),
    path('view/<int:id>/', ViewCompleteIdentity,name='view'),
]