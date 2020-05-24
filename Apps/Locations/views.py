from django.shortcuts import render, redirect, reverse
from Apps.Locations.models import *
from Apps.Locations.forms import *
from Apps.Cni.models import *
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def AddProvince(request):
    h3 = "Province"
    provinceForm = ProvinceForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if provinceForm.is_valid():
            province = provinceForm.cleaned_data['province']
            fullname_province_chief = provinceForm.cleaned_data['fullname_province_chief']
            Province(province = province, fullname_province_chief = fullname_province_chief).save()
            messages.success(request, "Enregistrer avec success !!!")
            provinceForm = ProvinceForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'province.html', locals() )


def AddCity(request):
    h3 = "Commune"
    cityForm = CityForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if cityForm.is_valid():
            city = cityForm.cleaned_data['city']
            province = cityForm.cleaned_data['province']
            fullname_city_chief = cityForm.cleaned_data['fullname_city_chief']
            City(city = city, fullname_city_chief = fullname_city_chief,province = province).save()
            messages.success(request, "Enregistrer avec success !!!")
            cityForm = CityForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'city.html', locals())
    

def AddArea(request):
    h3 = "Zone"
    areaForm = AreaForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if areaForm.is_valid():
            area = areaForm.cleaned_data['area']
            city = areaForm.cleaned_data['city']
            fullname_area_chief = areaForm.cleaned_data['fullname_area_chief']
            Area(area = area, fullname_area_chief = fullname_area_chief,city = city).save()
            messages.success(request, "Enregistrer avec success !!!")
            areaForm = AreaForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'area.html', locals() )

def AddDistrict(request):
    h3 = "Quartier"
    districtForm = DistrictForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if districtForm.is_valid():
            district = districtForm.cleaned_data['district']
            area = districtForm.cleaned_data['area']
            fullname_district_chief = districtForm.cleaned_data['fullname_district_chief']
            District(district = district, fullname_district_chief = fullname_district_chief,area = area).save()
            messages.success(request, "Enregistrer avec success !!!")
            districtForm = DistrictForm()
        else:
            messages.error(request, "Formulaire invalide !!!")
    return render(request, 'district.html', locals())
    
def TestingView(request):
    testingForm = TestingForm(request.POST or None, request.FILES)
    hand_over = request.POST.get('handover', None)
    show_hide_attest = "hidden"
    show_hide_confirm = "hidden"
    show_hide_cancel = "hidden"
    if request.method == "POST":
        if hand_over == "preview":
            if testingForm.is_valid():
                testing = testingForm.cleaned_data["testing"]
                show_hide_attest = "show"
                show_hide_form = "hidden"
                show_hide_preview = "hidden"
                show_hide_confirm = "show"
                show_hide_cancel = "show"

            else:
                messages.error(request, "Formulaire invalide !!!")

        if hand_over == "confirm":
            if testingForm.is_valid():
                testing = testingForm.cleaned_data["testing"]
                Testing(testing=testing).save()
                testingForm = TestingForm()
                messages.success(request, "Enregistrer avec success !!!")
                show_hide_attest = "hidden"

            else:
                messages.error(request, "Formulaire invalide !!!")
        # if testingForm.is_valid():
        #     testing = testingForm.cleaned_data["testing"]
        #     messages.success(request, "Ok one !!!")
        #     show_hide = "hidden"
        #     # return redirect(TestingViews)

        # else:
        #     messages.error(request, "Formulaire invalide !!!")
    return render(request, 'testing.html', locals())

def TestingViews(request):
    Secretary = "Secretary"
    connected_user = request.user
    # get_identity = CompleteIdentity.objects.filter(Q(beneficiary=connected_user) & Q(pk=id))
    get_prof = Profil.objects.filter(Q(user=connected_user))
    get_prof_c = Profil.objects.filter(Q(user=connected_user)).count()
    if get_prof_c < 0:
        messages.warning(request, "No profil found.")
    elif get_prof_c == 1:
        messages.warning(request, "Profil found.")
    return render(request,'views.html',locals()) 