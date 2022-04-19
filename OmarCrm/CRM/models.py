
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


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
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GA2 = models.CharField(max_length=100 , blank=True, null=True)
    GA3 = models.CharField(max_length=100 , blank=True, null=True)
    GA4 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField(default=False)
    GB2 = models.BooleanField(default=False)
    GB3 = models.BooleanField(default=False)
    GB4 = models.BooleanField(default=False)
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
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GA2 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField()
    GB2 = models.BooleanField()
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
    projectId = models.ForeignKey(ProjectInfoModel,on_delete=models.DO_NOTHING)
    assignDate = models.DateField(default=datetime.now)
    userLogin = models.ForeignKey(User,on_delete=models.SET_NULL , null=True , blank=True )


class commentsModel(models.Model):
    commentId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(CustomerInfoModel,on_delete=models.DO_NOTHING)
    projectId = models.ForeignKey(ProjectInfoModel,on_delete=models.DO_NOTHING)
    commentDate = models.DateField(default=datetime.now)
    comment = models.CharField(max_length=150)
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField()
    GD1 = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.commentDate} -- {self.customerId} -- {self.projectId} -- {self.comment}" 


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
    projectId = models.ForeignKey(ProjectInfoModel,on_delete=models.DO_NOTHING)
    paymentRef = models.CharField(max_length=100)
    transactionDate = models.DateField(default=datetime.now)
    paymentType = models.CharField(max_length=10 , choices=payType)
    paymentAmount = models.IntegerField()
    Currency = models.CharField(max_length=6 , choices=currency)
    GA1 = models.CharField(max_length=100 , blank=True, null=True)
    GB1 = models.BooleanField()
    GD1 = models.DateField(blank=True, null=True)


