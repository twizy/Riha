from django.urls import path
from Apps.Base.views import *
from Apps.CompleteIdentity.models import *
from Apps.Base.models import *

urlpatterns = [
    path('cl/', CompleteIdentityList, name='cl'), 
    path('cll/', AllCompleteIdentityList, name='cll'),
    path('view/<int:id>/', ViewCompleteIdentity, name='view'),
    path('', index, name='home'),
    path('edit_profil/<int:id>/', EditProfil, name='edit_profil'),
    path('accounts/login/', Connect, name='login'),
    path('register/', Inscription, name='register'),
    path('logout/', Disconnect, name = 'logout'),
    path('password/', Change_password, name='password'),
    path('step_2/', Step_two, name='step_2'),
]