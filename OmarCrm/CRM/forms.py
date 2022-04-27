from django import forms
from . models import CustomerInfoModel

class customerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfoModel
        fields = ('customerName','country','address','mobileNumber','workNumber','email','GD1')

        widgets = {
            'customerName' : forms.TextInput(attrs={'class':'form-control'} ),
            'country' : forms.Select(attrs={'class':'form-control'} ),
            'address' : forms.TextInput(attrs={'class':'form-control'} ),
            'mobileNumber' : forms.NumberInput(attrs={'class':'form-control'} ),
            'workNumber' : forms.NumberInput(attrs={'class':'form-control'} ),
            'email' : forms.EmailInput(attrs={'class':'form-control'} ),
            'GD1' : forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control' , 'placeholder':'yyyy-mm-dd (2025-07-28)'} ),
        }

        labels = {
            'customerName' : 'Customer Name',
            'mobileNumber' : 'Mobile Number',
            'workNumber' : 'Work Number',
            'GD1' : 'Contact Date'

        }