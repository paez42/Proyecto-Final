from django.urls import path

app_name = "aboutme"
from . import views

urlpatterns = [
    path("",views.home,name="home"),
]