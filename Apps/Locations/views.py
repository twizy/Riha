from django.shortcuts import render, redirect, reverse
from Apps.Locations.models import *
from Apps.Locations.forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def AddProvince(request):
    provinceForm = ProvinceForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if provinceForm.is_valid():
            province = provinceForm.cleaned_data['province']
            fullname_province_chief = provinceForm.cleaned_data['fullname_province_chief']
            city = provinceForm.cleaned_data['city']
            area = provinceForm.cleaned_data['area']
            district = provinceForm.cleaned_data['district']
            Province(province = province, fullname_province_chief = fullname_province_chief, city = city,area = area,district = district).save()
            messages.success(request, "Enregistrer avec success !!!")
            provinceForm = ProvinceForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'province.html', locals() )


def AddCity(request):
    cityForm = CityForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if cityForm.is_valid():
            city = cityForm.cleaned_data['city']
            fullname_city_chief = cityForm.cleaned_data['fullname_city_chief']
            City(city = city, fullname_city_chief = fullname_city_chief).save()
            messages.success(request, "Enregistrer avec success !!!")
            cityForm = CityForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'city.html', locals())
    

def AddArea(request):
    areaForm = AreaForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if areaForm.is_valid():
            area = areaForm.cleaned_data['area']
            fullname_area_chief = areaForm.cleaned_data['fullname_area_chief']
            Area(area = area, fullname_area_chief = fullname_area_chief).save()
            messages.success(request, "Enregistrer avec success !!!")
            areaForm = AreaForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'area.html', locals() )

def AddDistrict(request):
    districtForm = DistrictForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if districtForm.is_valid():
            district = districtForm.cleaned_data['district']
            fullname_district_chief = districtForm.cleaned_data['fullname_district_chief']
            District(district = district, fullname_district_chief = fullname_district_chief ).save()
            messages.success(request, "Enregistrer avec success !!!")
            districtForm = DistrictForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'district.html', locals() )