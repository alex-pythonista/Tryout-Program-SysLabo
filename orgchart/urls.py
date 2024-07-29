from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-employee/', views.add_employee, name='add-employee'),
    path('about-me/', views.aboutme, name='about-me'),
    path('common-department/', views.common_department, name='common-department'),
    path('add-department-info/', views.add_common_department, name='add-department-info'),
]