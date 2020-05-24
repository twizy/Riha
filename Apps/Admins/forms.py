from django import forms
from Apps.Admins.models import *
from Apps.Locations.models import *
from Apps.CompleteIdentity.models import *
from Apps.Locations.forms import *
from django.contrib.auth.models import User

class AdminUsersForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=User.objects.all().order_by('username'),
            label='Utilisateur')

    province = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Province.objects.all(),
            label='Birth Province')

    city = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=City.objects.all(),
            label='Birth City')

    area = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Area.objects.all(),
            label='Birth Area')

    district = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=District.objects.all(),
            label='Birth District')

    is_city_admin = forms.BooleanField(required=False)
    is_area_admin = forms.BooleanField(required=False)
    is_district_admin = forms.BooleanField(required=False)

    class Meta:
        model = AdminiUsers
        fields = "__all__"
        




