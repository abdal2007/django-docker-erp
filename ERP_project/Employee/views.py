from django.shortcuts import render
from Employee.models import Employee
from Employee.forms import EmployeeForm,MeetingForm
from ERP_project.forms import CreateUserForm
from django.contrib import messages
# Create your views here.
def AddEmployee(request):
    form = EmployeeForm()
    form2 = CreateUserForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        form2 = CreateUserForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            print("Form Saved")
            messages.success(request,"Form saved!")
        else:
            print('Form Error', form.errors)
            print('Form2 Error', form2.errors)
            messages.error(request, form.errors)    
            messages.error(request, form2.errors)    
    context = {'form':form}
    return render(request,'Employee/addEmployee.html', context)

def AddMeeting(request):
    member = Employee.objects.all()
    form = MeetingForm()
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form Saved!')
        else:
            print("form Error", form.errors)    

    context = {'member':member}
    return render(request, 'Employee/addmeeting.html', context)