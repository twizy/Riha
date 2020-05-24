from django.shortcuts import render, redirect, reverse, get_object_or_404
from Apps.Admins.models import *
from Apps.Locations.models import *
from Apps.Base.views import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse
from Apps.Admins.forms import *
from django.contrib import messages

# Create your views here.

@login_required
def attribute(request):
    h3 = "Attribue les roles."
    adminUsersForm = AdminUsersForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if adminUsersForm.is_valid():
            user = adminUsersForm.cleaned_data['user']
            province = adminUsersForm.cleaned_data['province']
            city = adminUsersForm.cleaned_data['city']
            area = adminUsersForm.cleaned_data['area']
            district = adminUsersForm.cleaned_data['district']
            is_city_admin = adminUsersForm.cleaned_data['is_city_admin']
            is_area_admin = adminUsersForm.cleaned_data['is_area_admin']
            is_district_admin = adminUsersForm.cleaned_data['is_district_admin']
            
            AdminiUsers(user=user, province=province, city=city, \
            area=area, district=district, is_city_admin=is_city_admin,\
            is_area_admin=is_area_admin, is_district_admin=is_district_admin).save()
            messages.success(request, "Enregistrer avec success !!!")
            adminUsersForm = AdminUsersForm()
            return redirect(index)

        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'roles.html', locals())