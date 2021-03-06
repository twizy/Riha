from django.shortcuts import render, redirect, reverse
from Apps.Cni.models import *
from Apps.Cni.forms import *
from Apps.Locations.models import *
from Apps.Locations.forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from Apps.Base.views import *
# Create your views here.

@login_required
def AddProfil(request):
    h3 = "Compléter votre profile"
    cniForm = CniForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if cniForm.is_valid():
            user = request.user
            genre = cniForm.cleaned_data['genre']
            no_identity = cniForm.cleaned_data['no_identity']
            given_place = cniForm.cleaned_data['given_place']
            birth_province = cniForm.cleaned_data['birth_province']
            birth_city = cniForm.cleaned_data['birth_city']
            birth_area = cniForm.cleaned_data['birth_area']
            birth_district = cniForm.cleaned_data['birth_district']
            birth_date = cniForm.cleaned_data['birth_date']
            father_fullname = cniForm.cleaned_data['father_fullname']
            mother_fullname = cniForm.cleaned_data['mother_fullname']
            profession = cniForm.cleaned_data['profession']
            phone_number = cniForm.cleaned_data['phone_number']
            matri_no = cniForm.cleaned_data['matri_no']
            residence_province = cniForm.cleaned_data['residence_province']
            residence_city = cniForm.cleaned_data['residence_city']
            residence_area = cniForm.cleaned_data['residence_area']
            residence_district = cniForm.cleaned_data['residence_district']
            civil_state = cniForm.cleaned_data['civil_state']
            
            Profil(user=user, genre=genre, no_identity=no_identity, given_place=given_place, \
            birth_province=birth_province, birth_city=birth_city, birth_area=birth_area,\
            birth_district=birth_district, birth_date=birth_date, father_fullname=father_fullname,\
            mother_fullname=mother_fullname, profession=profession, phone_number=phone_number,\
            matri_no=matri_no, residence_province=residence_province, residence_city=residence_city,\
            residence_area = residence_area, residence_district = residence_district, civil_state = civil_state).save()
            messages.success(request, "Enregistrer avec success !!!")
            cniForm = CniForm()
            return redirect(index)
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'profile.html', locals())
