from unicodedata import name
from . import views
from django.urls import path,include
from django.contrib import admin

urlpatterns=[
    path("Add_trip",views.Add_trip,name="Add_trip"),
    path("view_trip",views.view_trip,name="view_trip"),
    path("",views.register,name="register"),
    path("login",views.login,name="login"),
    path("register_function",views.register_function,name="register_function"),
    path("login_function",views.login_function,name="login_function"),
    path("logout",views.logout,name="logout"),
    path("add_trip_function",views.add_trip_function,name="add_trip_function"),
    path("edit_trip",views.edit_trip,name="edit_trip"),
    path("edit_trip_function",views.edit_trip_function,name="edit_trip_function")


]