from django.forms import ModelForm
from .models import SysUser


class SysUserForm(ModelForm):

    class Meta:
        model = SysUser
        fields = (
            'user_id', 'employee_number', 'department', 'email',
            'first_name', 'middle_name', 'last_name', 'gender',
            'home_phone', 'mobile_phone', 'title', 'manager'
        )
