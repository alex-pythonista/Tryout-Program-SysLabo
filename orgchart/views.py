from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView

# Create your views here.


class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')
    

class AddEmployeeView(CreateView):
    pass