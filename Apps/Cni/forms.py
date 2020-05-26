from django import forms
from Apps.Cni.models import *
from Apps.Locations.models import *
from Apps.Locations.forms import *

class CniForm(forms.ModelForm):
    genre = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Genre ','class':'form-control'}
            ),label='Genre')

    no_identity = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Indentity no ','class':'form-control'}
            ), label='Identity No')
            
    given_place = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Given date ','class':'form-control'}
            ), label='Given place')

    given_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Given place ','class':'form-control'}
            ), label='Given place')

    birth_province = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Province.objects.all(),
            label='Birth Province')

    birth_city = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=City.objects.all(),
            label='Birth City')

    birth_area = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Area.objects.all(),
            label='Birth Area')

    birth_district = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=District.objects.all(),
            label='Birth District')

    birth_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Road ','class':'form-control'}
            ), label='Birthday')

    father_fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Father full name ','class':'form-control'}
            ), label='Father full name')

    mother_fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Mother full name ','class':'form-control'}
            ), label='Mother full name')

    profession = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Profession ','class':'form-control'}
            ), label='Profession')

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':'Phone Number ','class':'form-control'}
            ), label='Phone Number')

    matri_no = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Matricule no', 'class': 'form-control'}
        ),label='Matricule no'
    )

    residence_province = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Province.objects.all(),
            label='Residence Province')

    residence_city = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=City.objects.all(),
            label='Residence City')

    residence_area = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Area.objects.all(),
            label='Residence Area')

    residence_district = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=District.objects.all(),
            label='Residence District')

    civil_state = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Civil state', 'class': 'form-control'}
        ),label='Civil state'
    )

    nationality = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nationality', 'class': 'form-control'}
        ),label='Nationality'
    )
    class Meta:
        model = Profil
        # fields = (
        #     "genre", "no_identity", "given_place", "road", "birth_province", "birth_city",
        #     "birth_area", "birth_district", "birth_date", "father_fullname", "mother_fullname", "profession",
        #     "phone_number", "matri_no", "residence_province", "residence_city", "residence_area", "residence_district","civil_state",
        #     )
        exclude = ("user","simple_user","staff_member","cni_one","cni_two",)
        




