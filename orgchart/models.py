from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.models import BaseModel
from .enums import (
    CalendarChoice, DateFormatChoice, TimeFormatChoice,
    GenderChoice, NotificationChoice, DepartmentChoice,
    DivisionChoice, SectionChoice, GroupChoice,
    TitleChoice
)
from .managers import UserManager

# Create your models here.
class SysUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    # user info
    sys_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="Sys ID")
    user_id = models.PositiveIntegerField(default=0, verbose_name="User ID")
    department = models.CharField(max_length=255, choices=DepartmentChoice.choices, blank=True, null=True)
    # department breakdown
    division = models.CharField(max_length=255, choices=DivisionChoice.choices, blank=True, null=True)
    section = models.CharField(max_length=255, choices=SectionChoice.choices, blank=True, null=True)
    group = models.CharField(max_length=255, choices=GroupChoice.choices, blank=True, null=True)

    email = models.EmailField(unique=True)
    employee_number = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="First Name")
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Middle Name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Name")
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GenderChoice.choices)
    home_phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Home Phone")
    mobile_phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mobile Phone")
    business_phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Business Phone")
    internal_integration_user = models.PositiveIntegerField(default=0, blank=True, verbose_name="Internal Integration User")
    prefix = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, choices=TitleChoice, blank=True, null=True)


    # other info
    building = models.CharField(max_length=255, blank=True, null=True)
    calendar_integration = models.CharField(max_length=255, choices=CalendarChoice.choices, blank=True, null=True, verbose_name="Calender Integration")
    ldap_server = models.CharField(max_length=255, blank=True, null=True, verbose_name="LDAP Server")
    location = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    notification = models.CharField(max_length=255, blank=True, default=NotificationChoice.DISABLED, choices=NotificationChoice.choices)
    language = models.CharField(max_length=255, blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    sso_source = models.CharField(max_length=255, blank=True, null=True)
    paid_days = models.PositiveIntegerField(default=0)
    vip_access_only = models.PositiveIntegerField(default=0, verbose_name="VIP	Web service access only")

    # address
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    cost_center = models.CharField(max_length=255, blank=True, null=True, verbose_name="Cost Center")
    country_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Country Code")
    state = models.CharField(max_length=255, blank=True, null=True, verbose_name="State / Province")
    street = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Zip / Postal Code")

    # date and time
    date_format = models.CharField(max_length=255, blank=True, null=True, choices=DateFormatChoice.choices, verbose_name="Date Format")
    time_format = models.CharField(max_length=255, blank=True, null=True, choices=TimeFormatChoice.choices, verbose_name="Time Format")
    defualt_perspective = models.CharField(max_length=255, blank=True, null=True)

    # security
    is_multifactor_enabled = models.BooleanField(default=False, blank=True, verbose_name="Enable Multifactor Authentication")
    failed_login = models.PositiveIntegerField(default=0, blank=True, verbose_name="Failed Login Attempts")
    password_needs_reset = models.BooleanField(default=False, blank=True, verbose_name="Password Needs Reset")

    # orm config
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Sys User"
        verbose_name_plural = "Sys Users"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}" or self.email
    

class CommonDepartment(models.Model):
    sys_id = models.UUIDField(primary_key=True, editable=False, default=uuid4, verbose_name="Sys ID")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Department Name")
    # department breakdown
    department = models.CharField(max_length=255, choices=DepartmentChoice.choices, blank=True, null=True)
    division = models.CharField(max_length=255, choices=DivisionChoice.choices, blank=True, null=True)
    section = models.CharField(max_length=255, choices=SectionChoice.choices, blank=True, null=True)
    group = models.CharField(max_length=255, choices=GroupChoice.choices, blank=True, null=True)

    ID = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    primary_contact =  models.ForeignKey(SysUser, on_delete=models.CASCADE, related_name="primary_contact")
    business_unit = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    cost_center = models.CharField(max_length=255, blank=True, null=True)
    department_head = models.ForeignKey(SysUser, on_delete=models.CASCADE, related_name="department_head")
    description = models.CharField(max_length=255, blank=True, null=True)
    head_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Common Department"
        verbose_name_plural = "Common Departments"

    def save(self, *args, **kwargs):
        # Concatenate department, division, section, and group
        components = filter(None, [self.department, self.division, self.section, self.group])
        self.name = ' '.join(components) or None
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


