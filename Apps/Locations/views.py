from django.shortcuts import render, redirect, reverse
from Apps.Locations.models import *
from Apps.Locations.forms import *
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def AddProvince(request):
    provinceForm = ProvinceForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if provinceForm.is_valid():
            province = provinceForm.cleaned_data['province']
            fullname_province_chief = provinceForm.cleaned_data['fullname_province_chief']
            city = provinceForm.cleaned_data['city']
            Province(province = province, fullname_province_chief = fullname_province_chief, city = city).save()
            msg = "Enregistrer avec success !!!"
        provinceForm = ProvinceForm()
    return render(request, 'province.html', locals() )


def AddCity(request):
    cityForm = CityForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if cityForm.is_valid():
            city = cityForm.cleaned_data['city']
            area = cityForm.cleaned_data['area']
            fullname_city_chief = cityForm.cleaned_data['fullname_city_chief']
            City(city = city, area = area, fullname_city_chief = fullname_city_chief).save()
            msg = "Enregistrer avec success !!!"
        cityForm = CityForm()
    return render(request, 'city.html', locals())
    

def AddArea(request):
    areaForm = AreaForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if areaForm.is_valid():
            area = areaForm.cleaned_data['area']
            fullname_area_chief = areaForm.cleaned_data['fullname_area_chief']
            district = areaForm.cleaned_data['district']
            Area(area = area, fullname_area_chief = fullname_area_chief, district = district).save()
            msg = "Enregistrer avec success !!!"
        areaForm = AreaForm()
    return render(request, 'area.html', locals() )

def AddDistrict(request):
    districtForm = DistrictForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if districtForm.is_valid():
            district = districtForm.cleaned_data['district']
            fullname_district_chief = districtForm.cleaned_data['fullname_district_chief']
            District(district = district, fullname_district_chief = fullname_district_chief ).save()
            msg = "Enregistrer avec success !!!"
        districtForm = DistrictForm()
    return render(request, 'district.html', locals() )