
from datetime import datetime
from django.db import models
from numpy import require


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
    startDate = models.DateField(default= datetime.now())
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