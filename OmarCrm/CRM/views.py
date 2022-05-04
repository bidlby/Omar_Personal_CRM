
from audioop import reverse
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView , list , ListView , UpdateView
from . models import CustomerInfoModel, assignProjectModel , ProjectInfoModel , commentsModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin 
from . forms import customerInfoForm, newCommentForm , projectInfoForm , assignProjectForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
  

#### end Create New 

## update views :

class updateProject(LoginRequiredMixin,UpdateView):
    template_name = 'CRM/NewProject.html'
    form_class = projectInfoForm
    model = ProjectInfoModel
    success_url = '/ProjectsList'

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

    def form_valid(self, form):
        form.instance.createdBy = self.request.user
        return super().form_valid(form)

### End Assign Project 

## Customer Profile 
@login_required
def customerProfile(request,pk):
    profile = CustomerInfoModel.objects.get(customerId = pk)

    context = {'profile':profile}
    return render(request,'CRM/CustomerProfile.html',context)

## Listس
@login_required
def customerList(request):
    customerListQuery = CustomerInfoModel.objects.all().filter(active = True)

    context = {'customerListQuery':customerListQuery}

    return render(request,'CRM/customerList.html',context)

@login_required
def ProjectsList(request):
    projectListQuery = assignProjectModel.objects.select_related('projectId_id').values_list('projectId__projectId','projectId__projectName','customerId__customerName','projectId__startDate','projectId__endDate','projectId__price','projectId__active','projectId__createdBy__username','userLogin').order_by('-projectId__startDate')

    context = {'projectListQuery':projectListQuery}

    return render(request,'CRM/projectList.html',context)


@login_required
def ProjectsHistoryList(request):
    projectListQuery = ProjectInfoModel.objects.all().filter(active = False)
    context = {'projectListQuery':projectListQuery}
    return render(request,'CRM/projectHistoryList.html',context)

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
        CustomerProjects = assignProjectModel.objects.filter(customerId = CustomerIDFilter)
    except Exception as e:
        CustomerProjects = ''


    context = {
     'q1':q1 ,
     'CustomerIDFilter':CustomerIDFilter,
     'CustomerProjects':CustomerProjects,
     'customerProfile':customerProfile,
     'loginUser' : loginUser
     }

    return render(request,'CRM/Profile.html',context)


