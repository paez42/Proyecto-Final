from django.urls import path

app_name = "cliente"
from . import views

urlpatterns = [
    path("",views.home, name="home"),
]
