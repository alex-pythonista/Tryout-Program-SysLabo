from django.forms import ModelForm

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.bootstrap import Div, Field

from .models import SysUser, CommonDepartment


class SysUserForm(ModelForm):

    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Field('user_id', wrapper_class='col-md-3'),
            # Field('employee_number', wrapper_class='col-md-3'),
            # department breakdown
            Field('department', wrapper_class='col-md-3'),
            Field('division', wrapper_class='col-md-3'),
            Field('section', wrapper_class='col-md-3'),
            Field('group', wrapper_class='col-md-3'),
            
            Field('email', wrapper_class='col-md-3'),
            Field('first_name', wrapper_class='col-md-3'),
            # Field('middle_name', wrapper_class='col-md-3'),
            Field('last_name', wrapper_class='col-md-3'),
            # Field('gender', wrapper_class='col-md-3'),
            # Field('home_phone', wrapper_class='col-md-3'),
            # Field('mobile_phone', wrapper_class='col-md-3'),
            Field('title', wrapper_class='col-md-3'),
            # Field('manager', wrapper_class='col-md-3'),
        css_class='form-row') 
    )
    helper.form_tag = False
    class Meta:
        model = SysUser
        fields = (
            'user_id', # 'employee_number', 
            'department', 'division', 'section', 'group', 
            'email',
            'first_name', 
            # 'middle_name', 
            'last_name', # 'gender',
            # 'home_phone', 'mobile_phone', 
            'title', # 'manager'
        )


class CommonDepartmentForm(ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Div(
                Field('department_head', wrapper_class='col-md-3'),
                Field('description', wrapper_class='col-md-3'),
                Field('head_count', wrapper_class='col-md-3'),
                Field('ID', wrapper_class='col-md-3'),
                Field('department', wrapper_class='col-md-3'),
                Field('division', wrapper_class='col-md-3'),
                Field('section', wrapper_class='col-md-3'),
                Field('group', wrapper_class='col-md-3'),
                Field('parent', wrapper_class='col-md-3'),
                Field('primary_contact', wrapper_class='col-md-3'),
                css_class='form-row'
            ), 
    )
    helper.form_tag = False
    class Meta:
        model = CommonDepartment
        fields = (
            'department_head', 'description', 'head_count', 'ID',
            'department', 'division', 'section', 'group',
            'parent', 'primary_contact',
        )