from django.contrib import admin
from .models import CustomerInfoModel , countryListModel , ProjectInfoModel

# Register your models here.

admin.site.register(CustomerInfoModel) , 
admin.site.register(countryListModel) , 
admin.site.register(ProjectInfoModel) , 

