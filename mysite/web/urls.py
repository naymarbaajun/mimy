from django.urls import path

from . import views

app_name='web'
urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login, name='login'),
    path('navigation',views.navigation, name='navigation'),
    path('employeedetails',views.employeedetails, name='employeedetails'),
    path('employee',views.Employee_list, name='employee')
     
]