from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.models import BaseModel
from .enums import (
    CalendarChoice, DateFormatChoice, GenderChoice
)

# Create your models here.
class SysUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    # user info
    department = models.CharField(max_length=255, blank=True, null=True) # wip
    email = models.EmailField(unique=True)
    employee_number = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Name")
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GenderChoice.choices)
    home_phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Home Phone")
    internal_integration_user = models.PositiveIntegerField(default=0, blank=True, verbose_name="Internal Integration User")
    prefix = models.CharField(max_length=255, blank=True, null=True)





    # other info
    building = models.CharField(max_length=255, blank=True, null=True)
    calendar = models.CharField(max_length=255, blank=True, null=True)
    calendar_integration = models.CharField(max_length=255, choices=CalendarChoice.choices, blank=True, null=True, verbose_name="Calender Integration")

    # address
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    cost_center = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cost Center")
    country_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Country Code")

    date_format = models.CharField(max_length=255, blank=True, null=True, choices=DateFormatChoice.choices, verbose_name="Date Format")
    defualt_perspective = models.CharField(max_length=255, blank=True, null=True)

    # security
    is_multifactor_enabled = models.BooleanField(default=False, blank=True, verbose_name="Enable Multifactor Authentication")
    falied_login = models.PositiveIntegerField(default=0, blank=True, verbose_name="Failed Login Attempts")
