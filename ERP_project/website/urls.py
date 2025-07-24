from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('ShowStaff/',views.ShowStaff, name = 'showStaff'),
    path('ShowStaffData/<int:id>/',views.ViewStaffData, name = 'viewStaffData'),
    path('Profile/',views.Profile, name = 'profile'),

]
