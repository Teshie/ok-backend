from django.db import models
from accounts.choices import  ManagingDepartmentChoice


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=25, default="Department")
    description = models.CharField(max_length=25, null=True, blank=True)
    managing_department = models.CharField(
        max_length=50, 
        choices=ManagingDepartmentChoice.choices, 
        default=ManagingDepartmentChoice.CEO, null=True, blank=True
    )
  
    def __str__(self):
        return self.name

class SubDepartment(models.Model):
    name = models.CharField(max_length=25, default="subdepartment")
    description = models.CharField(max_length=250, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="sub_departments")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Reports(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="reports")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class ReportSubDepartment(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    sub_department = models.ForeignKey(SubDepartment, on_delete=models.CASCADE, related_name="report_sub_departments")
    
    def __str__(self):
        return self.title

