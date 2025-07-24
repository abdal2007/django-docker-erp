from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from Employee.models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    employee = Employee.objects.first()
    context = {
        'employee':employee
    }

    return render(request,'website/dashboard.html', context)

def ShowStaff(request):
    data = User.objects.all()
    context = {'data':data}

    return render(request,'website/showStaff.html',context)

def ViewStaffData(request, id):
    data = User.objects.get(id=id)
    context = {'data':data}

    return render(request,'website/viewstaffdata.html',context)

@login_required
def Profile(request):
    employee = get_object_or_404(Employee, username=request.user.username)
    context = {
        'employee': employee
    }
    return render(request,'website/profile.html',context)


