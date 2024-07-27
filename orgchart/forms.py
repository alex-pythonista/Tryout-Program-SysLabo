from django.forms import ModelForm

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.bootstrap import Div, Field

from .models import SysUser


class SysUserForm(ModelForm):

    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Field('user_id', wrapper_class='col-md-3'),
            Field('employee_number', wrapper_class='col-md-3'),
            # department breakdown
            Field('department', wrapper_class='col-md-3'),
            Field('division', wrapper_class='col-md-3'),
            Field('section', wrapper_class='col-md-3'),
            Field('group', wrapper_class='col-md-3'),
            
            Field('email', wrapper_class='col-md-3'),
            Field('first_name', wrapper_class='col-md-3'),
            Field('middle_name', wrapper_class='col-md-3'),
            Field('last_name', wrapper_class='col-md-3'),
            Field('gender', wrapper_class='col-md-3'),
            Field('home_phone', wrapper_class='col-md-3'),
            Field('mobile_phone', wrapper_class='col-md-3'),
            Field('title', wrapper_class='col-md-3'),
            Field('manager', wrapper_class='col-md-3'),
        css_class='form-row') 
    )
    helper.form_tag = False
    class Meta:
        model = SysUser
        fields = (
            'user_id', 'employee_number', 
            'department', 'division', 'section', 'group', 
            'email',
            'first_name', 'middle_name', 'last_name', 'gender',
            'home_phone', 'mobile_phone', 'title', 'manager'
        )
