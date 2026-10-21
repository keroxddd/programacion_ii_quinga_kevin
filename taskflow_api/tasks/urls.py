# tasks/urls.py
from django.urls import path
from . import views

app_name = "tasks"   # namespace de la app — ver nota más abajo

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("admin", views.admin, name="admin"),
    path("saludo/<str:nombre>/",
         views.greeting, name="saludo"),
    path("my-first-template",
         views.my_first_template, name="my_first_template.html")
]