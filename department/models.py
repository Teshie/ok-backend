from django.db import models
from accounts.choices import  ManagingDepartmentChoice


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=25, null=True, blank=True)
    managing_department = models.CharField(
        max_length=50, 
        choices=ManagingDepartmentChoice.choices, 
        default=ManagingDepartmentChoice.CEO, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    
    
    
    def account(self):
        return self.accounts.first()
    
    def __str__(self):
        return self.name

class SubDepartment(models.Model):
    name = models.CharField(max_length=25, unique=True)
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
        return self.name

