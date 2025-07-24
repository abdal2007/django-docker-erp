from django.shortcuts import render
from .models import ProjectModel
from .forms import projectForm
from .models import ProjectCategoryModel

# Create your views here.

def CreateProject(request):
    cat = ProjectCategoryModel.objects.all()
    form = projectForm()
    if request.method == 'POST':
        form = projectForm(request.POST)

        if form.is_valid():
            form.save()
            print("form saved!")
        else:
            print("Form error :", form.errors)    
    context = {'form':form, 'cat':cat}
    return render(request,'Project/create_project.html', context)


def ShowprojectData(request):
    data = ProjectModel.objects.all()
    print("data: ", data)
    context= {'data':data}
    return render(request,'Project/showProjectData.html',context)