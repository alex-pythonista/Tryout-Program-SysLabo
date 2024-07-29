from django.shortcuts import render, redirect
from django.contrib import messages

from .models import CommonDepartment, SysUser
from .forms import SysUserForm, CommonDepartmentForm


def home(request, *args, **kwargs):
    return render(request, 'index.html')
    

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