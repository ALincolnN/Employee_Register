from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'employee_list.html')

def register(request):
    return


def delete(request):
    return