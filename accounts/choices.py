from django.db import models


class UserTypeChoices(models.TextChoices):
    CEO = 'CEO', "Chief Executive Officer"
    CMO = 'CMO', "Chief Executive Officer"
    CFO = 'CFO', "Chief Executive Officer"
    
class ManagingDepartmentChoice(models.TextChoices):
    CEO = 'CEO', "Chief Executive Officer"
    CMO = 'CMO', "Chief Managing Officer"
    CFO = 'CFO', "Chief Financial Officer"



