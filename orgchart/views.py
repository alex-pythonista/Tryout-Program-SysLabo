from django.shortcuts import render, redirect
from django.contrib import messages

from .models import SysUser
from .forms import SysUserForm


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

def aboutme(request, *args, **kwargs):
    return render(request, 'aboutme.html')