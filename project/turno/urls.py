from django.urls import path

app_name = "turno"
from . import views

# Turno Lugar
urlpatterns = [
    path("",views.home,name="home"),
    path("turnolugar/create/", views.TurnoLugarCreate.as_view(), name="turnolugar_create"),
    path("turnolugar/list/", views.TurnoLugarList.as_view(), name="turnolugar_list"),
    path("turnolugar/detail/<int:pk>", views.TurnoLugarDetail.as_view(), name="turnolugar_detail"),
    path("turnolugar/update/<int:pk>", views.TurnoLugarUpdate.as_view(), name="turnolugar_update"),
    path("turnolugar/delete/<int:pk>", views.TurnoLugarDelete.as_view(), name="turnolugar_delete"),
]

#Turno

urlpatterns += [
    path("turno/list", views.TurnoList.as_view(), name="turno_list"),
    path("turno/create", views.TurnoCreate.as_view(), name="turno_create"),
    path("turno/detail/<int:pk>", views.TurnoDetail.as_view(), name="turno_detail"),
    path("turno/update/<int:pk>", views.TurnoUpdate.as_view(), name="turno_update"),
    path("turno/delete/<int:pk>", views.TurnoDelete.as_view(), name="turno_delete"),
]