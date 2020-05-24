from django import forms
from .models import *
from django.contrib.auth.models import User
from Apps.Locations.models import *
from Apps.Locations.forms import *
from Apps.Cni.models import *
from Apps.CompleteIdentity.models import *

class ConnexionForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ', 'type':'password','class':'form-control'}))

class InscriptionForm(forms.Form):
    firstname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'First name ','class':'form-control'}), label='First name')
    lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Last name ','class':'form-control'}), label='Last name')
    username = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}), label='Username')
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')
    email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'Email address ','class':'form-control'} ), label='Email address')
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Avatar')

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Old password ','type':'password','class':'form-control col-xl-12 col-lg-12 col-12'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'New password ', 'type':'password','class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password ', 'type': 'password', 'class': 'form-control'}))
    

class CniForm3(forms.ModelForm):
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
        exclude = ("user","simple_user",)


class TreatedCompleteIdentityForm(forms.ModelForm):

    treated = forms.BooleanField(required=False)
    correct = forms.BooleanField(required = False)

    class Meta:
        model = CompleteIdentity
        fields = (
            "treated","correct",
            )


