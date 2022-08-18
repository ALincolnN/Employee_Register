from importlib.metadata import files
from select import select
from django import forms
from . models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'emp_code' : 'Employee Code',
            'mobile': 'Mobile Number',
            'position' : 'Job Description'
            
            



        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label= 'select'