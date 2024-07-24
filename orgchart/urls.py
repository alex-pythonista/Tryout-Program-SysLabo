from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-employee/', views.add_employee, name='add-employee'),
]