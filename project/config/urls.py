from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("cliente/", include("cliente.urls")),
    path("turno/", include("turno.urls")),
]