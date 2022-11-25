from django.contrib import admin

from .models import *
#register 
admin.site.register(Department)
admin.site.register(SubDepartment)
admin.site.register(Reports)
admin.site.register(ReportSubDepartment)


