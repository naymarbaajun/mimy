from django.shortcuts import render
from django.http import HttpResponse
from.models import Employee
from.forms import Employeeform
# Create your views here.

def home(request):
    
    return render(request =request,template_name='home.html')


def login(request):

    return render(request=request,template_name='login.html')

def navigation(request):
    return render(request=request,template_name='navigation.html')

def employeedetails(request):
    if request.method =="POST":
       

        Employee_form=Employeeform(request.POST)
        if Employee_form.is_valid():
            Employee_form.save()
        else:
            messages.error(request,('your details is invalid'))
    Employee_form=Employeeform()        
    return render(request=request, template_name="employeedetails.html",context={'Employee_form':Employee_form})      



def Employee_list(request):
    emp=Employee.objects.all()
    return render(request=request,template_name="employeelist.html",context={"emp":emp})  
           



