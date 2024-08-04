from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CommonDepartment, SysUser
from .forms import SysUserForm, CommonDepartmentForm
from .utils import get_sales_department, get_system_department, get_support_people

def home(request, *args, **kwargs):
    # sales_dept = SysUser.objects.filter(department='営業本部')
    sales_dept = get_sales_department()
    system_dept = get_system_department()
    support = get_support_people()
    data = {
        "sales": sales_dept,
        "system": system_dept,
        "support": support,
    }
    
    return render(request, 'index.html', context=data)
    

def add_employee(request, *args, **kwargs):
    form = SysUserForm()
    if request.method == "POST":
        form = SysUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'A new employee added')
            return redirect('home')

    return render(request, 'add_employee.html', context={
        'form': form
    })

def common_department(request, *args, **kwargs):
    data = CommonDepartment.objects.all()
    return render(request, 'department_info.html', context={
        'data': data,
    })

def add_common_department(request, *args, **kwargs):
    form = CommonDepartmentForm()
    if request.method == "POST":
        form = CommonDepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'A new department info added')
            return redirect('common-department')

    return render(request, 'add_dept_info.html', context={
        'form': form
    })
    

def aboutme(request, *args, **kwargs):
    return render(request, 'aboutme.html')