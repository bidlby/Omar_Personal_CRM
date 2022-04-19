
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import CreateView , list , ListView
from . models import CustomerInfoModel

# Create your views here.

def test(request):
    x = 'basel'
    return render(request,'CRM/index.html',{'x':x})


class NewCustomerInfo(CreateView):
    template_name = 'CRM/NewCustomer.html'
    model = CustomerInfoModel
    fields = ('customerName','country','address','mobileNumber','workNumber')
    success_url = '/test'

def customerList(request):
    customerListQuery = CustomerInfoModel.objects.all()

    context = {'customerListQuery':customerListQuery}

    return render(request,'CRM/customerList.html',context)





