
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.

class countryListModel(models.Model):
    countryId = models.AutoField(primary_key=True)
    countryName = models.CharField(max_length=50,unique=True)

    def __str__(self) -> str:
        return f"{self.countryName}"

class CustomerInfoModel(models.Model):
    customerId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=100 , unique=True)
    country = models.ForeignKey(countryListModel,on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=150)
    mobileNumber = models.IntegerField(unique=True)
    workNumber = models.IntegerField()
    email = models.EmailField(max_length=50 , unique=True)
    userLogin = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="b" ,  on_delete=models.DO_NOTHING , null=True , blank=True )
    createdBy = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GA2 = models.CharField(max_length=100 , blank=True, null=True)
    GA3 = models.CharField(max_length=100 , blank=True, null=True)
    GA4 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField(default=False , blank=True, null=True)
    GB2 = models.BooleanField(default=False , blank=True, null=True)
    GB3 = models.BooleanField(default=False , blank=True, null=True)
    GB4 = models.BooleanField(default=False , blank=True, null=True)
    GD1 = models.DateField(blank=True, null=True)
    GD2 = models.DateField(blank=True, null=True)
    GD3 = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.customerName}"

class ProjectInfoModel(models.Model):
    projectId = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=100 , unique=True)
    projectDesc =  models.CharField(max_length=300)
    startDate = models.DateField(default= datetime.now)
    endDate = models.DateField(blank=True, null=True)
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GA2 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField(default=False , blank=True, null=True)
    GB2 = models.BooleanField(default=False , blank=True, null=True)
    GD1 = models.DateField(blank=True, null=True)
    GD2 = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.projectName}"

class projectContractModel(models.Model):

    cs_period = [
        ('3 Month', '3 Month'),
        ('6 Month', '6 Month'),
        ('9 Month', '9 Month'),
        ('12 Month', '12 Month'),
        ]

    contractId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(CustomerInfoModel,on_delete=models.DO_NOTHING)
    projectId = models.ForeignKey(ProjectInfoModel,on_delete=models.DO_NOTHING)
    contractPeriod = models.CharField(max_length=10, choices=cs_period)
    startDate = models.DateField(default=datetime.now)
    endDate = models.DateField(blank=True, null=True)
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField()
    GD1 = models.DateField(blank=True, null=True)

class assignProjectModel(models.Model):
    assignId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(CustomerInfoModel,on_delete=models.DO_NOTHING)
    projectId = models.OneToOneField(ProjectInfoModel,on_delete=models.DO_NOTHING)
    assignDate = models.DateField(default=datetime.now)
    userLogin = models.CharField(max_length=50, null=True , blank=True )
    createdBy = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def save(self, *args , **kwargs):
        self.userLogin = CustomerInfoModel.objects.values('userLogin__username').filter(customerName = self.customerId)
        super().save(*args, **kwargs) 

    def __str__(self) -> str:
        return f"{self.userLogin} - {self.projectId}"

class commentsModel(models.Model):
    commentId = models.AutoField(primary_key=True)
    projectId = models.ForeignKey(ProjectInfoModel,on_delete=models.DO_NOTHING)
    commentDate = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length=400)
    createdBy = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField(blank=True, null=True)
    GD1 = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.projectId} -- {self.commentDate}  -- {self.projectId} -- {self.comment}" 


class paymentsModel(models.Model):

    payType = [
            ('Card', 'Card'),
            ('Cash', 'Cash')
            ]
    
    currency = [
        ('AED','AED'),
        {'$' , 'dollar'}
    ]

    transactionId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(CustomerInfoModel,on_delete=models.DO_NOTHING)
    paymentRef = models.CharField(max_length=100)
    transactionDate = models.DateField(default=datetime.now)
    paymentType = models.CharField(max_length=10 , choices=payType)
    paymentAmount = models.IntegerField()
    Currency = models.CharField(max_length=6 , choices=currency)
    createdBy = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField(blank=True, null=True)
    GD1 = models.DateField(blank=True, null=True)


## Test Model :

class testModel(models.Model):
    customerIdt = models.ForeignKey(CustomerInfoModel, on_delete=models.DO_NOTHING)
    userLogint = models.CharField(max_length=10 )
    
    def save(self, *args , **kwargs):
        self.userLogint = CustomerInfoModel.objects.values('userLogin__username').filter(customerName = self.customerIdt)
        super().save(*args, **kwargs)

