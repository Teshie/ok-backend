from django.db import models


class UserTypeChoices(models.TextChoices):
    CEO = 'CEO', "Chief Executive Officer"
    HoD = 'HoD', "Department Head"
    SUB = 'SUB', "Sub Department"
    CLIENT_ADMIN = 'CLIENT_ADMIN', "Client Admin"
    
class ManagingDepartmentChoice(models.TextChoices):
    CEO = 'CEO', "Chief Executive Officer"
    CMO = 'CMO', "Chief Managing Officer"
    CFO = 'CFO', "Chief Financial Officer"



