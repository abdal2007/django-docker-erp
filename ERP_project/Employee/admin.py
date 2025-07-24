from django.contrib import admin
from Employee.models import *
from django.utils.html import format_html

from django.contrib import admin
from .models import Employee
from django.utils.html import format_html

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'img_preview')  # 👈 this is key

    def img_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover;" />', obj.img.url)
        return "No Image"

    img_preview.short_description = 'Image'

admin.site.register(Employee, EmployeeAdmin)

# Register your models here.
admin.site.register(Dept)

admin.site.register(Meeting)
