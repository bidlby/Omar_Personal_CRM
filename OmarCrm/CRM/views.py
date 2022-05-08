

from importlib.resources import path
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView , list , ListView , UpdateView , DeleteView
from . models import CustomerInfoModel, assignProjectModel , ProjectInfoModel , commentsModel, paymentsModel , testModel , customerPaymentAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin 
from . forms import customerInfoForm, newCommentForm , projectInfoForm , assignProjectForm , paymentsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Count , Max , F , Min , Q , Sum 
from django.db.models.functions import TruncMonth , TruncYear

### Authintaion :

class signUpView(LoginRequiredMixin,CreateView):
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

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class NewProject(LoginRequiredMixin,CreateView):
    template_name = 'CRM/NewProject.html'
    form_class = projectInfoForm
    model = ProjectInfoModel
    success_url = '/customerList'

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

class NewComment(LoginRequiredMixin,CreateView):
    template_name = 'CRM/NewComment.html'
    form_class = newCommentForm
    model = commentsModel
    #success_url = '/customerList'

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

    ## default Value for NewComment
    def get_initial(self):
        projectId = get_object_or_404(ProjectInfoModel, pk=self.kwargs['pk'])


        return {
        'projectId': projectId,
        }  

    def get_context_data(self, **kwargs):
       context = super(NewComment, self).get_context_data(**kwargs)
       context['queryset'] = ProjectInfoModel.objects.filter(pk= self.kwargs['pk'])
       context['CommentList'] = commentsModel.objects.filter(projectId = self.kwargs['pk']).order_by('-commentDate')

       print(context)

       return context

    def get_success_url(self):
       return reverse_lazy('CRM:NewComment' , kwargs={'pk': self.kwargs['pk']})
  
class NewPaymentView(LoginRequiredMixin,CreateView):
    template_name = 'CRM/NewPayment.html'
    form_class = paymentsForm
    model = paymentsModel
    success_url = '/PaymentHitoryList'

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)


#### end Create New 

## update views :

class updateProject(LoginRequiredMixin,UpdateView):
    template_name = 'CRM/NewProject.html'
    form_class = projectInfoForm
    model = ProjectInfoModel
    success_url = '/ProjectsList'

class testView(LoginRequiredMixin,CreateView):
    template_name = 'CRM/ZTestView.html'
    #form_class = projectInfoForm
    fields = ('customerIdt',)
    model = testModel
    success_url = '/testView'

class updateCustomerProfile(LoginRequiredMixin,UpdateView):
    template_name = 'CRM/customerProfileUpdate.html'
    form_class = customerInfoForm
    #fields = ['customerName']
    model = CustomerInfoModel
    success_url = '/customerList'

### Assign Project :

class AssignPojectView(LoginRequiredMixin,CreateView):
    template_name = 'CRM/AssignProject.html'
    form_class = assignProjectForm

    model = assignProjectModel
    success_url = '/customerList'

    def get_form(self, *args, **kwargs):
        form = super(AssignPojectView, self).get_form(*args, **kwargs)
        filter = assignProjectModel.objects.values('projectId_id')
        OpenProject = ProjectInfoModel.objects.exclude(projectId__in = filter)
        form.fields['projectId'].queryset = ProjectInfoModel.objects.filter(projectId__in = OpenProject)
        return form

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

### End Assign Project 

#### Deletes
#################

class deletePayment(LoginRequiredMixin,DeleteView):
    #template_name = 'CRM/NewPayment.html'
    model = paymentsModel
    success_url = '/PaymentHitoryList'


## Customer Profile 
@login_required
def customerProfile(request,pk):
    profile = CustomerInfoModel.objects.get(customerId = pk)

    context = {'profile':profile}
    return render(request,'CRM/CustomerProfile.html',context)

## List
@login_required
def customerList(request):
    customerListQuery = CustomerInfoModel.objects.all().filter(active = True)

    context = {'customerListQuery':customerListQuery}

    return render(request,'CRM/customerList.html',context)

@login_required
def ProjectsList(request):
    projectListQuery = assignProjectModel.objects.select_related('projectId_id').values_list('projectId__projectId','projectId__projectName','customerId__customerName','projectId__startDate','projectId__endDate','projectId__price','projectId__active','projectId__createdBy__username','userLogin').filter(projectId__active=True).order_by('-projectId_id')
    context = {'projectListQuery':projectListQuery}

    return render(request,'CRM/projectList.html',context)


@login_required
def ProjectsHistoryList(request):
    projectListQuery = assignProjectModel.objects.select_related('projectId_id').values_list('projectId__projectId','projectId__projectName','customerId__customerName','projectId__startDate','projectId__endDate','projectId__price','projectId__active','projectId__createdBy__username','userLogin').filter(projectId__active=False).order_by('-projectId_id')

    context = {'projectListQuery':projectListQuery}
    return render(request,'CRM/projectHistoryList.html',context)


@login_required
def PaymentHistory(request):
    PyamentHitoryList = paymentsModel.objects.all().order_by('-transactionId')

    context = {'PyamentHitoryList':PyamentHitoryList}
    return render(request,'CRM/PaymentHistoryList.html',context)

## By User itself:
@login_required
def UserCheckProject(request):

    loginUser = User.objects.filter(username = request.user)

    try:
        customerProfile = CustomerInfoModel.objects.filter(userLogin =  loginUser[0])
    except Exception as e:
        customerProfile = ''

    try:
        q1 = assignProjectModel.objects.filter(userLogin = request.user)
    except Exception as e:
        q1 = 'NO Projects'

    try:
        CustomerIDFilter = q1.values_list('customerId')[0]
    except Exception as e:
        CustomerIDFilter = 'NO Projects'
    try:
        CustomerProjects = assignProjectModel.objects.values('projectId__projectName','assignDate','projectId__price','projectId__active','projectId__endDate').filter(customerId = CustomerIDFilter)
    except Exception as e:
        CustomerProjects = ''

    try:
        CustomerPayment = paymentsModel.objects.values('customerId__customerName','transactionDate','paymentType','paymentAmount','Currency').filter(customerId = CustomerIDFilter).order_by('-transactionDate')
    except Exception as e:
        CustomerPayment = ''

    context = {
     'q1':q1 ,
     'CustomerIDFilter':CustomerIDFilter,
     'CustomerProjects':CustomerProjects,
     'customerProfile':customerProfile,
     'loginUser' : loginUser,
     'CustomerPayment' : CustomerPayment
     }

    return render(request,'CRM/Profile.html',context)



#### Reports :
## ACcounting Open Balance 

def financeBalance (request):
    
    # Open
    SOA_OpenBalance = customerPaymentAccount.objects.values('customerId','customerName').annotate(totalCredit = Sum('credit') , totalDebit = Sum('debit') , openBalance = F('totalCredit')-F('totalDebit')).filter(openBalance__gt = 0).order_by('-openBalance')

    #Closed
    SOA_ClosedBalance = customerPaymentAccount.objects.values('customerId','customerName').annotate(totalCredit = Sum('credit') , totalDebit = Sum('debit') , openBalance = F('totalCredit')-F('totalDebit')).filter(openBalance = 0).order_by('-customerId')

    context = {'SOA_OpenBalance':SOA_OpenBalance,'SOA_ClosedBalance':SOA_ClosedBalance}

    return render(request,'CRM/financeOpenBalance.html',context)

def CustomerAccountBalance (request,pk):
    Soa_Customer = customerPaymentAccount.objects.values('customerId','customerName').annotate(totalCredit = Sum('credit') , totalDebit = Sum('debit') , openBalance = F('totalCredit')-F('totalDebit')).filter(customerId = pk)

    SoaDtl_Customer = customerPaymentAccount.objects.all().filter(customerId = pk)


    context = {'Soa_Customer':Soa_Customer,'SoaDtl_Customer':SoaDtl_Customer}

    return render(request,'CRM/financeCustomerBalance.html',context)

## Total Projects : 
def projectMonthlyReport (request):

    if request.method == 'POST':
        yearFilter = request.POST['yearFilter']   
        projectListQuery = customerPaymentAccount.objects.values(year = TruncYear('transactionDate') , month = TruncMonth('transactionDate')).annotate(TDebit = Sum('debit') ,TCredit = Sum('credit') , TCount = Count('credit')).filter(transactionDate__year = yearFilter).order_by('-month')

        context = {'projectListQuery':projectListQuery}
        return render(request,'CRM/MonthlyReport.html',context)
    else:
        projectListQuery = customerPaymentAccount.objects.values(year = TruncYear('transactionDate') , month = TruncMonth('transactionDate')).annotate(TDebit = Sum('debit') ,TCredit = Sum('credit') , TCount = Count('credit')).order_by('-month')
        context = {'projectListQuery':projectListQuery}
        return render(request,'CRM/MonthlyReport.html',context)


### Test :

def testView2(request):

    filter = assignProjectModel.objects.values('projectId_id')
    OpenProject = ProjectInfoModel.objects.exclude(projectId__in = filter)

    #filter(product=product, preparation__id__not_in=preparations)
    context = {'Q1':OpenProject}


    return render(request,'CRM/ZTest.html',context)
