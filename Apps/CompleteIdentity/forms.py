from django import forms
from Apps.Cni.models import *
from Apps.Locations.models import *
from Apps.CompleteIdentity.models import *


class CompleteIdentityForm(forms.ModelForm):

    area = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Area.objects.all(),
            label='Area')

    birth_year = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Année de naissance', 'class': 'form-control'}
            ),
            label='Année de naissance')

    transaction_code = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Code de Transaction', 'class': 'form-control'}
            ),
            label='Transaction code')
            

    class Meta:
        model = CompleteIdentity
        fields = (
            "birth_year","transaction_code","area",
            )

