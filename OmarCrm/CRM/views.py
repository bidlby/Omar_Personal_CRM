from django.shortcuts import render

# Create your views here.

def test(request):
    x = 'basel'
    return render(request,'CRM/index.html',{'x':x})