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

    city = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': 'City', 'class': 'form-control'}
            ), queryset = City.objects.all(),
            label = 'City')

    class Meta:
        model = Province
        fields = "__all__"


class CityForm(forms.ModelForm):
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'City ','class':'form-control'}
            ), label='City', max_length=100)
            
    area = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': 'Area', 'class': 'form-control'}
            ), queryset=Area.objects.all(),
            label='Area')

    fullname_city_chief = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Full name of city chief','class':'form-control'}
            ), label='City chief', max_length=100)

    class Meta:
        model = City
        fields = "__all__"


class AreaForm(forms.ModelForm):
    area = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Area ','class':'form-control'}
            ), label='Area', max_length=100)

    fullname_area_chief = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Full name of area chief','class':'form-control'}
            ), label='Area chief', max_length=100)

    district = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': 'District', 'class': 'form-control'}
            ), queryset = District.objects.all(),
            label = 'District')
            
    class Meta:
        model = Area
        fields = "__all__"


class DistrictForm(forms.ModelForm):
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
        fields = "__all__"