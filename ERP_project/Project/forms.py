from django.forms import ModelForm
from .models import *

class projectForm(ModelForm):
    class Meta:
        model = ProjectModel
        fields = '__all__'
    
    
