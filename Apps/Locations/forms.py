from django import forms
from Apps.Locations.models import *

class ProvinceForm(forms.ModelForm):
    province = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Province ','class':'form-control'}
            ), label='Province', max_length=100)
            
    fullname_province_chief = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Full name of province chief','class':'form-control'}
            ), label='Province', max_length=100)
            
    class Meta:
        model = Province
        fields = "__all__"

class CityForm(forms.ModelForm):

    province = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Province.objects.all(),
            label='Province')

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'City ','class':'form-control'}
            ), label='City', max_length=100)
 
    fullname_city_chief = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Full name of city chief','class':'form-control'}
            ), label='City chief', max_length=100)

    class Meta:
        model = City
        fields = ("province","city","fullname_city_chief")


class AreaForm(forms.ModelForm):

    city = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': 'City', 'class': 'form-control'}
            ), queryset = City.objects.all(),
            label='City')

    area = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Area ','class':'form-control'}
            ), label='Area', max_length=100)

    fullname_area_chief = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Full name of area chief','class':'form-control'}
            ), label='Area chief', max_length=100)


    class Meta:
        model = Area
        fields = ("city","area","fullname_area_chief")


class DistrictForm(forms.ModelForm):

    area = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': 'Area', 'class': 'form-control'}
            ), queryset=Area.objects.all(),
            label='Area')

    district = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'District', 'class': 'form-control'}
        ),label='District', max_length=100
    )

    fullname_district_chief = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Full name of district chief', 'class': 'form-control'}
        ),label='District chief', max_length=100
    )

    class Meta:
        model = District
        fields = ("area", "district", "fullname_district_chief")
        
class TestingForm(forms.ModelForm):

    testing = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Testing 1','class':'form-control'}
            ), label='Testing', max_length=100)

    class Meta:
        model = Testing
        fields = "__all__"
