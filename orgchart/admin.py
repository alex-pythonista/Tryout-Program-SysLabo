from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SysUser, CommonDepartment

@admin.register(SysUser)
class SysUserAdmin(UserAdmin):
    search_fields = ("email", "first_name", "employee_number")
    list_display = ("first_name", "email", "employee_number")
    ordering = ("-sys_id",)
    fieldsets = (
        (
            'Credentials',
            {
                'fields': (
                    'email',
                    'password',
                )
            },
        ),
        (
            'Personal Info',
            {
                'fields': (
                    'user_id',
                    'department',
                    'division',
                    'section',
                    'group',
                    'employee_number',
                    'first_name',
                    'middle_name',
                    'last_name',
                    'gender',
                    'home_phone',
                    'business_phone',
                    'mobile_phone',
                    'internal_integration_user',
                    'prefix',
                    'title',
                )
            },
        ),
        (
            'Other Info',
            {
                'fields': (
                    'building',
                    'calendar_integration',
                    'ldap_server',
                    'location',
                    'manager',
                    'notification',
                    'language',
                    'schedule',
                    'source',
                    'sso_source',
                    'paid_days',
                    'vip_access_only',
                )
            },
        ),
        (
            'address',
            {
                'fields': (
                    'city',
                    'company',
                    'cost_center',
                    'country_code',
                    'state',
                    'street',
                    'zip_code'
                )
            },
        ),
        (
            'Date and Time',
            {
                'fields': (
                    'date_format',
                    'time_format',
                ),
            },
        ),
        (
            'security',
            {
                'fields': (
                    'is_multifactor_enabled',
                    'failed_login',
                    'password_needs_reset',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_verified',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
    )
    add_fieldsets = (
        (
            'Click save and continue editing',
            {   
                'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
            },
        ),
    )    

@admin.register(CommonDepartment)
class CommonDepartAdmin(admin.ModelAdmin):
    pass