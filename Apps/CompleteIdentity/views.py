from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    get_prof = Profil.objects.filter(Q(user=beneficiary))
    h3 = "Complete identity"
    
    counter = Profil.objects.filter(user=beneficiary).count()
    hand_over = request.POST.get('handover', None)
    show_hide_attest = "hidden"
    show_hide_confirm = "hidden"
    show_hide_cancel = "hidden"

    if request.method == "POST":
        if hand_over == "preview":
            if completeIdentityForm.is_valid():
                province            = completeIdentityForm.cleaned_data['province']
                city                = completeIdentityForm.cleaned_data['city']
                area                = completeIdentityForm.cleaned_data['area']
                payment_type        = completeIdentityForm.cleaned_data['payment_type']
                transaction_code    = completeIdentityForm.cleaned_data['transaction_code']
                show_hide_attest    = "show"
                show_hide_form      = "hidden"
                show_hide_preview   = "hidden"
                show_hide_confirm   = "show"
                show_hide_cancel    = "show"

            else:
                messages.error(request, "Formulaire invalide !!!")

        if hand_over == "confirm":
            if completeIdentityForm.is_valid():
                province            = completeIdentityForm.cleaned_data['province']
                city                = completeIdentityForm.cleaned_data['city']
                area                = completeIdentityForm.cleaned_data['area']
                payment_type        = completeIdentityForm.cleaned_data['payment_type']
                transaction_code    = completeIdentityForm.cleaned_data['transaction_code']
            
                CompleteIdentity(beneficiary=beneficiary, transaction_code=transaction_code,
                province = province,city = city,area = area,payment_type = payment_type).save()
                
                messages.success(request, "Enregistrer avec success !!!")
                show_hide_attest = "hidden"
                completeIdentityForm = CompleteIdentityForm()
            else:
                messages.error(request, "Formulaire invalide !!!")

    return render(request, 'completeIdentity.html', locals())
