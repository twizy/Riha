from django.shortcuts import render, redirect, reverse, get_object_or_404
from Apps.Cni.models import *
from Apps.Locations.models import *
from Apps.CompleteIdentity.models import *
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def Index(request):
    h3 = "Acceuil"
    return render(request,'base.html',locals())

def CompleteIdentityList(request):
    connected_user = request.user
    get_identity = CompleteIdentity.objects.filter(beneficiary=connected_user)
    return render(request,'home.html',locals())

def ViewCompleteIdentity(request, id):
    Secretary = "Secretary"
    connected_user = request.user
    get_identity = CompleteIdentity.objects.filter(Q(beneficiary=connected_user) & Q(pk=id))
    get_prof = Profil.objects.filter(Q(user=connected_user))
    return render(request,'view.html',locals()) 