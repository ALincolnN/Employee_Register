from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.

def index(request):
    return render(request, 'base.html')

def register(request):
    form = EmployeeForm()
    return render(request, 'employee_form.html',{'form':form})


def delete(request):
    return render(request, 'employee_list.html')