from django import forms
from Apps.Cni.models import *
from Apps.Locations.models import *
from Apps.CompleteIdentity.models import *
from Apps.Base.models import *


class CompleteIdentityForm(forms.ModelForm):

    province = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Province.objects.all().order_by('province'),
            label='Province')

    city = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=City.objects.all().order_by('city'),
            label='City')


    area = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=Area.objects.all().order_by('area'),
            label='Area')

    payment_type = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': '', 'class': 'form-control'}
            ), queryset=PaymentType.objects.all(),
            label='Payment type')

    transaction_code = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Code de Transaction', 'class': 'form-control'}
            ),
            label='Transaction code')
        

    class Meta:
        model = CompleteIdentity
        fields = (
            "payment_type","transaction_code","province",
            )

