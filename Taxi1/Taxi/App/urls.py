from . import views
from django.urls import path,include
from django.contrib import admin

urlpatterns=[
    path("",views.Add_trip,name="Add_trip"),
    path("view_trip",views.view_trip,name="view_trip"),
    


]