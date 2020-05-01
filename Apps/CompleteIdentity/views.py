from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from Apps.Cni.models import *
from Apps.Locations.models import *
from Apps.CompleteIdentity.forms import *
from Apps.CompleteIdentity.models import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def AddCompleteIdentity(request):
    completeIdentityForm = CompleteIdentityForm(request.POST or None, request.FILES)
    beneficiary = request.user
    get_area_location = Area.objects.all()[:1]
    get_all_user_details = Profil.objects.filter(user=beneficiary)
    counter = Profil.objects.filter(user=beneficiary).count()


    if request.method == "POST":
        if completeIdentityForm.is_valid():
            province            = completeIdentityForm.cleaned_data['province']
            birth_year          = completeIdentityForm.cleaned_data['birth_year']
            transaction_code    = completeIdentityForm.cleaned_data['transaction_code']
        
            CompleteIdentity(beneficiary=beneficiary, birth_year=birth_year, transaction_code=transaction_code,province = province).save()
            
            messages.success(request, "Enregistrer avec success !!!")
            completeIdentityForm = CompleteIdentityForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'completeIdentity.html', locals())
