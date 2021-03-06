"""OmarCrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path 
from . import views 
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

app_name = 'CRM'

urlpatterns = [
    path('',RedirectView.as_view(url='accounts/login')),
    path('',views.test,name='home'),
    path('NewCustomerInfo',views.NewCustomerInfo.as_view() , name='NewCustomerInfo'),
    path('NewComment/<int:pk>',views.NewComment.as_view() , name='NewComment'),
    path('NewProject',views.NewProject.as_view() , name='NewProject'),
    path('updateProject/<int:pk>',views.updateProject.as_view() , name='updateProject'),
    path('AssignPoject',views.AssignPojectView.as_view() , name='AssignPoject'),
    path('customerList',views.customerList , name='customerList'),
    path('UserCheckProject',views.UserCheckProject,name='UserCheckProject'),
    path('signUp',views.signUpView.as_view(),name='signUp'),
    path('customerProfile/<int:pk>',views.customerProfile,name='customerProfile'),
    path('updateCustomerProfile/<int:pk>',views.updateCustomerProfile.as_view(),name='updateCustomerProfile'),
    path('ProjectsList',views.ProjectsList,name='ProjectsList'),
    path('ProjectsHistoryList',views.ProjectsHistoryList,name='ProjectsHistoryList'),
    path('testView',views.testView.as_view(),name='testView'),
    path('NewPayment',views.NewPaymentView.as_view(),name='NewPayment'),
    path('PaymentHitoryList',views.PaymentHistory,name='PaymentHitoryList'),
    path('deletePayment/<int:pk>',views.deletePayment.as_view(),name='deletePayment'),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('financeOpenBalance', views.financeBalance ,name='financeOpenBalance'),
    path('financeClosedBalance', views.financeBalance ,name='financeClosedBalance'),
    path('CustomerBalance/<int:pk>', views.CustomerAccountBalance ,name='CustomerBalance'),
    path('PRMonthly', views.projectMonthlyReport ,name='PRMonthly'),
    path('testView2', views.testView2 ,name='testView2'),



  

]
