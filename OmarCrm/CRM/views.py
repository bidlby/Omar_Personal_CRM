
from distutils.log import error
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView , list , ListView
from . models import CustomerInfoModel, assignProjectModel , ProjectInfoModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import customerInfoForm , projectInfoForm , assignProjectForm
from django.contrib.auth.forms import UserCreationForm

### Authintaion :

class signUpView(CreateView):
    form_class = UserCreationForm    
    success_url = reverse_lazy('login')
    template_name = 'CRM/signUp.html'

#####

# Create your views here.

def test(request):
    x = 'basel'
    return render(request,'CRM/index.html',{'x':x})

### Create New :

class NewCustomerInfo(LoginRequiredMixin,CreateView):
    template_name = 'CRM/NewCustomer.html'
    form_class = customerInfoForm
    model = CustomerInfoModel
    success_url = '/customerList'

class NewProject(LoginRequiredMixin,CreateView):
    template_name = 'CRM/NewProject.html'
    form_class = projectInfoForm
    model = ProjectInfoModel
    success_url = '/customerList'


#### end Create New 

### Assign Project :

class AssignPojectView(LoginRequiredMixin,CreateView):
    template_name = 'CRM/AssignProject.html'
    form_class = assignProjectForm
    model = assignProjectModel
    success_url = '/customerList'

### End Assign Project 

def customerList(request):
    customerListQuery = CustomerInfoModel.objects.all()

    context = {'customerListQuery':customerListQuery}

    return render(request,'CRM/customerList.html',context)

#@login_required
def UserCheckProject(request):

    try:
        q1 = assignProjectModel.objects.filter(userLogin = request.user)
    except Exception as e:
        q1 = ''

    CustomerIDFilter = q1.values_list('customerId')[0]
    
    CustomerProjects = assignProjectModel.objects.filter(customerId = CustomerIDFilter)

    customerProfile = CustomerInfoModel.objects.filter(customerId =  CustomerIDFilter[0])


    context = {
     'q1':q1 ,
     'CustomerIDFilter':CustomerIDFilter,
     'CustomerProjects':CustomerProjects,
     'customerProfile':customerProfile
     }

    return render(request,'CRM/Profile.html',context)


