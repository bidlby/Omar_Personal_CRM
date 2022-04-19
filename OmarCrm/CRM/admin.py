from django.contrib import admin
from .models import CustomerInfoModel , countryListModel , ProjectInfoModel , assignProjectModel , projectContractModel , paymentsModel , commentsModel

# Register your models here.

admin.site.register(CustomerInfoModel) , 
admin.site.register(countryListModel) , 
admin.site.register(ProjectInfoModel) , 
admin.site.register(assignProjectModel) , 
admin.site.register(projectContractModel) , 
admin.site.register(paymentsModel) , 
admin.site.register(commentsModel) , 

