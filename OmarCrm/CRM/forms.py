from django import forms
from . models import CustomerInfoModel , ProjectInfoModel , assignProjectModel, commentsModel , paymentsModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget



### Authentaion 

#####



#####

class customerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfoModel
        fields = ('customerName','country','address','mobileNumber','workNumber','email','GD1','userLogin')

        GD1 = forms.DateField(widget=AdminDateWidget())

        widgets = {
            'customerName' : forms.TextInput(attrs={'class':'form-control'} ),
            'country' : forms.Select(attrs={'class':'form-control'} ),
            'address' : forms.TextInput(attrs={'class':'form-control'} ),
            'mobileNumber' : forms.NumberInput(attrs={'class':'form-control'} ),
            'workNumber' : forms.NumberInput(attrs={'class':'form-control'} ),
            'email' : forms.EmailInput(attrs={'class':'form-control'} ),
            'GD1' : forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control' , 'placeholder':'yyyy-mm-dd (2025-07-28)'} ),
            #'GD1' : forms.DateInput(format='%d/%m/%Y'),
            'userLogin' : forms.Select(attrs={'class':'form-control'})
        }

        labels = {
            'customerName' : 'Customer Name',
            'mobileNumber' : 'Mobile Number',
            'workNumber' : 'Work Number',
            'GD1' : 'Contact Date'
        }

class projectInfoForm(forms.ModelForm):
    class Meta:
        model = ProjectInfoModel
        fields = ('projectName','projectDesc','startDate','endDate','price','active')

        widgets = {
            'projectName' : forms.TextInput(attrs={'class':'form-control'} ),
            'projectDesc' : forms.Textarea(attrs={'class':'form-control'} ),
            'startDate' : forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control' , 'placeholder':'yyyy-mm-dd (2025-07-28)'} ),
            'endDate' : forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control' , 'placeholder':'yyyy-mm-dd (2025-07-28)'} ),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
        }

        labels = {
            'projectName' : 'Project Name',
            'projectDesc' : 'Project Desc',
            'startDate' : 'Start Date',
            'endDate' : 'End Date',
            'price' : 'Price',
            'active' : 'Acitve',
        }

class assignProjectForm(forms.ModelForm):
    class Meta:
        model = assignProjectModel
        fields = ('customerId','projectId','assignDate')

        widgets = {
            'customerId' : forms.Select(attrs={'class':'form-control'} ),
            'projectId' : forms.Select(attrs={'class':'form-control'} ),
            'assignDate' : forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control' , 'placeholder':'yyyy-mm-dd (2025-07-28)'} ),
            'userLogin' : forms.Select(attrs={'class':'form-control'} ),            
            'createdBy' : forms.Select(attrs={'class':'form-control'} ),            
        }

        labels = {
            'customerId' : 'Customer Name',
            'projectId' : 'Project Desc',
            'assignDate' : 'Start Date',
            'userLogin' : 'User Name',
            'createdBy' : 'createdBy Name',
        }

            

class newCommentForm(forms.ModelForm):
    class Meta:
        model = commentsModel
        fields = ('projectId','comment')

        widgets = {
            'projectId' : forms.Select(attrs={'class':'form-control' , 'hidden': 'True'} ),
            'comment' : forms.Textarea(attrs={'class':'form-control'} ),            
        }

        labels = {
            'projectId' : '',
            'comment' : 'Comment',
        }


class paymentsForm(forms.ModelForm):
    class Meta:
        model = paymentsModel
        fields = ('customerId','paymentRef','transactionDate','paymentType','paymentAmount','Currency')

        widgets = {
            'customerId' : forms.Select(attrs={'class':'form-control'} ),
            'paymentRef' : forms.TextInput(attrs={'class':'form-control'} ),
            'transactionDate' : forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control' , 'placeholder':'yyyy-mm-dd (2025-07-28)'} ),
            'paymentType' : forms.Select(attrs={'class':'form-control'} ),            
            'Currency' : forms.Select(attrs={'class':'form-control'} ),    
            'paymentAmount' : forms.NumberInput(attrs={'class':'form-control'} ),    

                    
        }

        labels = {
            'customerId' : 'Customer Name',
            'paymentRef' : 'Payment Desc',
            'transactionDate' : 'Transaction Date',
            'paymentType' : 'Payment Type',
            'Currency' : 'Currency',
            'paymentAmount' : 'Amount',
        }